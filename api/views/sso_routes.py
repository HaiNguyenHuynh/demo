import os

from flask import Blueprint, redirect, request, session
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from werkzeug.exceptions import NotFound

from services.user_services import get_user_by_email, create_user

sso_bp = Blueprint("saml2", __name__)


# Helper function to prepare Flask request for SAML
def init_saml_auth(req):
    saml_settings_path = os.path.join(os.getcwd(), "saml")
    auth = OneLogin_Saml2_Auth(req, custom_base_path=saml_settings_path)
    return auth


def prepare_flask_request(request):

    return {
        "https": "on" if request.scheme == "https" else "off",
        "http_host": request.host,
        "script_name": request.path,
        "server_port": request.environ["SERVER_PORT"],
        "get_data": request.args.copy(),
        "post_data": request.form.copy(),
    }


@sso_bp.route("/login")
def login():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    return redirect(auth.login())


@sso_bp.route("/acs/", methods=["POST"])
def acs():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    auth.process_response()
    errors = auth.get_errors()

    if len(errors) == 0:
        is_sso = True
        data = auth.get_attributes()
        user_claim_name = data[
            "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"
        ][0]
        user_role = data[
            "http://schemas.microsoft.com/ws/2008/06/identity/claims/role"
        ][0]
        user_give_name = data[
            "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname"
        ][0]
        user_surname = data[
            "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname"
        ][0]
        try:
            user_info = get_user_by_email(user_claim_name)
        except NotFound:
            profile_data = {
                "first_name": user_give_name,
                "last_name": user_surname,
            }
            create_user(
                email=user_claim_name,
                password="",
                role_name=user_role,
                profile_data=profile_data,
                is_sso=is_sso,
            )
            user_info = get_user_by_email(user_claim_name)
        session["user_id"] = user_info["id"]
        session["samlUserdata"] = auth.get_attributes()
        session["samlNameId"] = auth.get_nameid()
        session["is_sso"] = is_sso
        if user_info["role"] == "Admin":
            response = redirect("/users")
        else:
            response = redirect("/")
        response.set_cookie("role", user_info["role"])
        return response
    print(errors)
    return f"SAML Authentication failed: {errors}", 400


@sso_bp.route("/metadata/")
def metadata():
    saml_settings_path = os.path.join(os.getcwd(), "saml")
    auth = OneLogin_Saml2_Auth(
        prepare_flask_request(request), custom_base_path=saml_settings_path
    )
    saml_settings = auth.get_settings()
    metadata = saml_settings.get_sp_metadata()
    errors = saml_settings.validate_metadata(metadata)

    if len(errors) == 0:
        return metadata, 200

    return ", ".join(errors), 500

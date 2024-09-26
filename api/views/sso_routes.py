"""
This module contains the SAML SSO routes for user authentication and authorization
using the OneLogin SAML library. It handles login, logout, and metadata routes,
as well as processing SAML responses.
"""

import os

from flask import Blueprint, redirect, request, session
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from werkzeug.exceptions import NotFound

from services.user_services import get_user_by_email, create_user

sso_bp = Blueprint("saml2", __name__)


# Helper function to prepare Flask request for SAML
def init_saml_auth(req):
    """
    Initialize OneLogin SAML authentication with the custom base path for SAML settings.

    Args:
        req (dict): A dictionary of request data prepared for SAML.

    Returns:
        OneLogin_Saml2_Auth: An instance of OneLogin SAML authentication.
    """
    saml_settings_path = os.path.join(os.getcwd(), "saml")
    auth = OneLogin_Saml2_Auth(req, custom_base_path=saml_settings_path)
    return auth


def prepare_flask_request(flask_request):
    """
    Prepare the Flask request data for SAML authentication.

    Args:
        flask_request (Request): The Flask request object.

    Returns:
        dict: A dictionary containing request information for SAML processing.
    """
    return {
        "https": "on" if request.scheme == "https" else "off",
        "http_host": flask_request.host,
        "script_name": flask_request.path,
        "server_port": flask_request.environ["SERVER_PORT"],
        "get_data": flask_request.args.copy(),
        "post_data": flask_request.form.copy(),
    }


@sso_bp.route("/login")
def login():
    """
    Initiate the SAML login process and redirect the user to the SAML IdP.

    Returns:
        Response: A redirect response to the SAML IdP login page.
    """
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    return redirect(auth.login())


@sso_bp.route("/acs/", methods=["POST"])
def acs():
    """
    Process the SAML assertion consumer service (ACS) response from the IdP.

    Returns:
        Response: Redirects the user to the home page on successful authentication.
                  Returns a 400 error response if SAML authentication fails.
    """
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


@sso_bp.route("/logout")
def logout():
    """
    Log out the user from the SAML session.

    Returns:
        Response: A redirect response to the IdP logout URL.
    """
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    return redirect(auth.logout(name_id=session["samlNameId"]))


@sso_bp.route("/metadata/")
def metadata():
    """
    Provide the SAML metadata for the Service Provider (SP).

    Returns:
        Response: The metadata XML if valid, or an error response if validation fails.
    """
    saml_settings_path = os.path.join(os.getcwd(), "saml")
    auth = OneLogin_Saml2_Auth(
        prepare_flask_request(request), custom_base_path=saml_settings_path
    )
    saml_settings = auth.get_settings()
    sp_metadata = saml_settings.get_sp_metadata()
    errors = saml_settings.validate_metadata(sp_metadata)

    if len(errors) == 0:
        return sp_metadata, 200

    return ", ".join(errors), 500

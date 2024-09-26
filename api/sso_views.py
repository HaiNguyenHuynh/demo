from flask import Blueprint, redirect, request, session, url_for, render_template
from onelogin.saml2.auth import OneLogin_Saml2_Auth

# from onelogin.saml2.utils import OneLogin_Saml2_Utils
import os


sso_views = Blueprint("saml2", __name__, url_prefix="/saml2")


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


@sso_views.route("/login")
def login():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    return redirect(auth.login())


@sso_views.route("/acs/", methods=["POST"])
def acs():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    auth.process_response()
    errors = auth.get_errors()

    if len(errors) == 0:
        session["samlUserdata"] = auth.get_attributes()
        session["samlNameId"] = auth.get_nameid()
        return redirect("/saml2/home")
    else:
        return "SAML Authentication failed", 400


@sso_views.route("/home")
def home():
    if "samlUserdata" in session:
        userdata = session["samlUserdata"]
        return render_template("home.html", userdata=userdata)
    else:
        return redirect("/saml2/login")


@sso_views.route("/logout")
def logout():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    return redirect(auth.logout(name_id=session["samlNameId"]))


@sso_views.route("/metadata/")
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
    else:
        return ", ".join(errors), 500

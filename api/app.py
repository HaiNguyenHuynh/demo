from flask import Flask, redirect, request, session, url_for, render_template
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from onelogin.saml2.utils import OneLogin_Saml2_Utils
import os

from database import db
from views import views

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = "averylongsecretkey"

db.init_app(app)

app.register_blueprint(views)

@app.route("/")
def index():
    return "Hello, World!"

# Helper function to prepare Flask request for SAML
def init_saml_auth(req):
    saml_settings_path = os.path.join(os.getcwd(), 'saml')
    auth = OneLogin_Saml2_Auth(req, custom_base_path=saml_settings_path)
    return auth

def prepare_flask_request(request):
    url_data = request.url.split('?')
    return {
        'https': 'on' if request.scheme == 'https' else 'off',
        'http_host': request.host,
        'script_name': request.path,
        'server_port': request.environ['SERVER_PORT'],
        'get_data': request.args.copy(),
        'post_data': request.form.copy(),
    }

@app.route('/')
def index():
    return 'Welcome to Flask SAML SSO App!'

@app.route('/login')
def login():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    return redirect(auth.login())

@app.route('/acs', methods=['POST'])
def acs():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    auth.process_response()
    errors = auth.get_errors()

    if len(errors) == 0:
        session['samlUserdata'] = auth.get_attributes()
        session['samlNameId'] = auth.get_nameid()
        return redirect(url_for('home'))
    else:
        return "SAML Authentication failed", 400

@app.route('/home')
def home():
    if 'samlUserdata' in session:
        userdata = session['samlUserdata']
        return render_template('home.html', userdata=userdata)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    return redirect(auth.logout(name_id=session['samlNameId']))

@app.route('/metadata/')
def metadata():
    saml_settings_path = os.path.join(os.getcwd(), 'saml')
    auth = OneLogin_Saml2_Auth(prepare_flask_request(request), custom_base_path=saml_settings_path)
    saml_settings = auth.get_settings()
    metadata = saml_settings.get_sp_metadata()
    errors = saml_settings.validate_metadata(metadata)

    if len(errors) == 0:
        return metadata, 200
    else:
        return ', '.join(errors), 500


if __name__ == "__main__":
    app.run(debug=True)

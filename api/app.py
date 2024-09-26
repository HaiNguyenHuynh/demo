from flask import Flask
from views.api_routes import api_bp
from views.sso_routes import sso_bp
from database.models import db

# Initialize the Flask application
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object("config.Config")

# Initialize the database with the app
db.init_app(app)


# Register Blueprints
app.register_blueprint(api_bp, url_prefix="/api")  # API routes at /api/*
app.register_blueprint(sso_bp, url_prefix="/sso")  # SSO routes at /sso/*


# Default route (for testing, can be customized or removed)
@app.route("/")
def home():
    return "Welcome to Flask SAML SSO App!"


# Run the application
if __name__ == "__main__":
    app.run(debug=True)

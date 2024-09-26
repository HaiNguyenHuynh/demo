import os
from config import DevelopmentConfig, ProductionConfig
from flask import Flask
from flask_talisman import Talisman
from cli.commands import register_commands
from database.models import db
from views.api_routes import api_bp
from views.sso_routes import sso_bp


# Initialize the Flask application
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object("config.Config")
talisman = Talisman(app, content_security_policy=None)

if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# Initialize the database with the app
db.init_app(app)


# Register Blueprints
app.register_blueprint(api_bp)  # API routes at /api/*
app.register_blueprint(sso_bp, url_prefix="/saml2")  # SSO routes at /sso/*

# Register custom CLI commands
register_commands(app)


# Run the application
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

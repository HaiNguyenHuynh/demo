"""
This module initializes the Flask app, registers blueprints,
sets up the database, and defines custom CLI commands for the application.
"""

from flask import Flask, render_template
from cli.commands import register_commands
from database.models import db
from views.api_routes import api_bp
from views.sso_routes import sso_bp


# Initialize the Flask application
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object("config.Config")

# Initialize the database with the app
db.init_app(app)


# Register Blueprints
app.register_blueprint(api_bp, url_prefix="/api")  # API routes at /api/*
app.register_blueprint(sso_bp, url_prefix="/saml2")  # SSO routes at /sso/*

# Register custom CLI commands
register_commands(app)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    """
    Render the index page for the application.

    Args:
        path (str): The path requested.

    Returns:
        Response: The rendered index page.
    """
    return render_template("index.html")


# Run the application
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

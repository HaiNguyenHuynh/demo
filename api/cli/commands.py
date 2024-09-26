from flask import current_app as app
from flask.cli import with_appcontext
from database.models import db, Role
import click


# Command to initialize the database (create all tables)
@click.command("init-db")
@with_appcontext
def init_db():
    """
    Initialize the database and create tables based on models.
    """
    db.create_all()
    click.echo("Database initialized!")


# Command to create default roles (Admin and User)
@click.command("create-roles")
@with_appcontext
def create_roles():
    """
    Create default roles (Admin, User).
    """
    # Check if roles already exist
    if not Role.query.filter_by(name="Admin").first():
        db.session.add(Role(name="Admin"))
        click.echo("Created Admin role.")
    if not Role.query.filter_by(name="User").first():
        db.session.add(Role(name="User"))
        click.echo("Created User role.")

    # Commit the changes to the database
    db.session.commit()
    click.echo("Roles created successfully!")


# Function to register CLI commands with the Flask app
def register_commands(app):
    app.cli.add_command(init_db)
    app.cli.add_command(create_roles)

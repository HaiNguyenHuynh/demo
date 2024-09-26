from flask import current_app as app
from database import db
from database import Role

# Constants for roles
ADMIN_ROLE = "Admin"
USER_ROLE = "User"


@app.cli.command("create-roles")
def create_roles():
    """
    Custom command to create default roles (Admin and User).
    Run this command using 'flask create-roles'
    """
    if not Role.query.filter_by(name=ADMIN_ROLE).first():
        db.session.add(Role(name=ADMIN_ROLE))
    if not Role.query.filter_by(name=USER_ROLE).first():
        db.session.add(Role(name=USER_ROLE))

    db.session.commit()
    print("Roles Admin and User created successfully!")


@app.cli.command("init-db")
def init_db():
    """
    Initialize the database and create tables.
    Run this command using 'flask init-db'
    """
    db.create_all()
    print("Database initialized!")

# pylint: disable=unused-argument, missing-module-docstring

import pytest
from app import app
from database.models import db, Role


@pytest.fixture(scope="module")
def test_client():
    """
    Set up the Flask test client and initialize the in-memory database.
    """
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # In-memory database
    app.config["WTF_CSRF_ENABLED"] = False  # Disable CSRF for testing

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Create all tables in the in-memory database
            yield testing_client  # This is where the testing happens
            db.session.remove()
            db.drop_all()  # Clean up after tests


@pytest.fixture(scope="module")
def setup_roles():
    """
    Set up default roles in the in-memory database.
    """
    with app.app_context():
        admin_role = Role(name="Admin")
        user_role = Role(name="User")
        db.session.add_all([admin_role, user_role])
        db.session.commit()

# pylint: disable=unused-argument, missing-module-docstring

from werkzeug.security import generate_password_hash
from app import app
from database.models import User, db


def test_get_user_list(test_client, setup_roles):
    """
    Test the GET /users route to fetch all users.
    """
    # Create a user to test fetching
    hashed_password = generate_password_hash("password123")
    new_user = User(email="testuser@example.com", password=hashed_password, role_id=2)

    # Ensure app context is used for db session operations
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()

    # Fetch the user list
    response = test_client.get("/api/users")

    # Check that the response is valid
    assert response.status_code == 200
    assert response.is_json, "Response content is not JSON"

    json_data = response.get_json()

    # Check if json_data is None
    assert json_data is not None, "Response JSON is None"

    # Proceed to test the contents of the response
    assert len(json_data) == 1  # Ensure the length is 1 as one user was created
    assert json_data[0]["email"] == "testuser@example.com"

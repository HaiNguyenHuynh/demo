"""
This module provides API routes for managing users, including user registration,
authentication, profile management, and SAML-based SSO support.
"""

# pylint: disable=broad-exception-caught

from flask import jsonify, Blueprint, redirect, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash

from views.sso_routes import init_saml_auth, prepare_flask_request
from auth import authorize
from database.models import User, Role, db


ADMIN_ROLE_ID = 1


api_bp = Blueprint("views", __name__)


@api_bp.route("/users", methods=["GET"])
def get_user_list():
    """
    Fetch a list of all users.

    Returns:
        Response: A JSON response containing a list of users or an error message.
    """
    try:
        users = User.query.all()
        user_list = [
            {"id": user.id, "email": user.email, "is_sso": user.is_sso}
            for user in users
        ]
        return jsonify(user_list), 200
    except Exception as error:  # Use a more specific exception if possible
        return jsonify({"error": str(error)}), 500


@api_bp.route("/users", methods=["POST"])
@authorize(ADMIN_ROLE_ID)
def create_user():
    """
    Create a new user with the default role.

    Returns:
        Response: A JSON response indicating success or an error message.
    """
    default_role_id = 2
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        hashed_password = generate_password_hash(password)

        new_user = User(email=email, role_id=default_role_id, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"data": "OK"}), 201
    except Exception as error:  # Use a more specific exception if possible
        db.session.rollback()
        return jsonify({"error": str(error)}), 500


@api_bp.route("/login", methods=["POST"])
def login():
    """
    Authenticate a user with their email and password.

    Returns:
        Response: A JSON response indicating success or an error message.
    """
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first_or_404()
        role = Role.query.get(user.role_id)

        if not check_password_hash(user.password, password):
            return jsonify({"error": "Invalid email or password"}), 400

        session["user_id"] = user.id
        response = jsonify({"data": "OK"})
        response.set_cookie("role", role.name)
        return response, 200

    except Exception as error:  # Use a more specific exception if possible
        return jsonify({"error": str(error)}), 500


@api_bp.route("/register", methods=["POST"])
def register():
    """
    Register a new user with the default role.

    Returns:
        Response: A JSON response indicating success or an error message.
    """
    default_role_id = 2
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        hashed_password = generate_password_hash(password)

        new_user = User(email=email, role_id=default_role_id, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"data": "OK"}), 200
    except Exception as error:  # Use a more specific exception if possible
        db.session.rollback()
        return jsonify({"error": str(error)}), 500


@api_bp.route("/logout", methods=["POST", "GET"])
def logout():
    """
    Log the user out, clearing the session.

    Returns:
        Response: A redirect response to the logout page or home.
    """
    if session.get("is_sso"):
        req = prepare_flask_request(request)
        auth = init_saml_auth(req)
        response = redirect(auth.logout(name_id=session.get("samlNameId")))
    else:
        response = redirect("/")
    session.clear()
    response.delete_cookie("role")
    return response


@api_bp.route("/me", methods=["GET"])
@authorize()
def get_own_profile():
    """
    Fetch the profile of the currently logged-in user.

    Returns:
        Response: A JSON response containing the user's profile data.
    """
    current_user = g.user
    return jsonify({"email": current_user.email}), 200

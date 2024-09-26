"""
This module provides services related to user management, including
user creation, retrieval of user details by ID or email, and fetching users by role.
"""

from database.models import db, User, Role, Profile


def create_user(email, password, role_name, profile_data=None, is_sso=False):
    """
    Create a new user with the given email, password, and role.
    Optionally, add profile information and specify if the user is created via SSO.

    Args:
        email (str): The email of the new user.
        password (str): The password for the new user.
        role_name (str): The role assigned to the new user.
        profile_data (dict, optional): Profile details (first name, last name, etc.).
        is_sso (bool, optional): Whether the user is created via SSO.

    Returns:
        dict: A dictionary containing a success message and the user's ID or an error message.
    """
    # Check if the email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {"error": "A user with this email already exists."}, 400

    # Find the role by name
    role = Role.query.filter_by(name=role_name).first()
    if not role:
        return {"error": f"Role '{role_name}' does not exist."}, 400

    # Create a new User object
    new_user = User(
        email=email,
        password=password,
        role=role,
        is_sso=is_sso,
    )

    # Create a Profile for the user, if profile data is provided
    if profile_data:
        new_profile = Profile(
            first_name=profile_data.get("first_name"),
            last_name=profile_data.get("last_name"),
            date_of_birth=profile_data.get("date_of_birth"),
            bio=profile_data.get("bio"),
            user=new_user,
        )
        db.session.add(new_profile)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return {"message": "User created successfully", "user_id": new_user.id}, 201


def get_all_users():
    """
    Retrieve all users from the database.

    Returns:
        list: A list of dictionaries containing user details.
    """
    users = User.query.all()
    user_data = []

    for user in users:
        user_info = {
            "id": user.id,
            "email": user.email,
            "role": user.role.name,
            "profile": {
                "first_name": user.profile.first_name if user.profile else None,
                "last_name": user.profile.last_name if user.profile else None,
                "date_of_birth": user.profile.date_of_birth if user.profile else None,
                "bio": user.profile.bio if user.profile else None,
            },
        }
        user_data.append(user_info)

    return user_data


def get_user_by_id(user_id):
    """
    Retrieve a user by their ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing the user's details.
    """
    user = User.query.get_or_404(user_id)
    user_info = {
        "id": user.id,
        "email": user.email,
        "role": user.role.name,
        "profile": {
            "first_name": user.profile.first_name if user.profile else None,
            "last_name": user.profile.last_name if user.profile else None,
            "date_of_birth": user.profile.date_of_birth if user.profile else None,
            "bio": user.profile.bio if user.profile else None,
        },
    }
    return user_info


def get_user_by_email(email):
    """
    Query a user by their email.

    Args:
        email (str): The email of the user to retrieve.

    Returns:
        dict: A dictionary containing the user's details.
    """
    user = User.query.filter_by(email=email).first_or_404()
    user_info = {
        "id": user.id,
        "email": user.email,
        "role": user.role.name,
        "profile": {
            "first_name": user.profile.first_name if user.profile else None,
            "last_name": user.profile.last_name if user.profile else None,
            "date_of_birth": user.profile.date_of_birth if user.profile else None,
            "bio": user.profile.bio if user.profile else None,
        },
    }
    return user_info


def get_users_by_role(role_name):
    """
    Retrieve users associated with a specific role.

    Args:
        role_name (str): The name of the role.

    Returns:
        list: A list of dictionaries containing the details of users with the given role.
    """
    role = Role.query.filter_by(name=role_name).first_or_404()
    users = role.users  # Access users associated with this role

    user_data = []
    for user in users:
        user_info = {
            "id": user.id,
            "email": user.email,
            "profile": {
                "first_name": user.profile.first_name if user.profile else None,
                "last_name": user.profile.last_name if user.profile else None,
                "date_of_birth": user.profile.date_of_birth if user.profile else None,
                "bio": user.profile.bio if user.profile else None,
            },
        }
        user_data.append(user_info)

    return user_data

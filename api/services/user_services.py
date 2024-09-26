from database.models import db, User, Role, Profile


def create_user_logic(email, password, role_name, profile_data=None, is_sso=False):
    """
    Create a new user with the given email, password, and role.
    Optionally, add profile information and specify if the user is created via SSO.
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
    Query user by email.
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

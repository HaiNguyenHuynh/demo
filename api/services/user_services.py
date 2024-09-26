from database.models import User, Role


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

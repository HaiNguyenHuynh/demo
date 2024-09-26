"""
This module provides user authentication and authorization functionality,
including a decorator to check user roles before accessing a resource.
"""

from functools import wraps
from flask import jsonify, session, g
from database.models import User


# Simple example of a user authentication check function
def check_authorization(role_id: int | None):
    """
    Check if the current user is authorized to access a resource.

    Args:
        role_id (int | None): The role ID required to access the resource.
                              If None, any authenticated user can access.

    Returns:
        bool: True if the user is authorized, False otherwise.
    """
    # In a real app, you'd verify the user session, token, or API key here
    # This is just a simple placeholder logic for demonstration
    user = User.query.get(session.get("user_id"))
    if not user:
        print("GET HERE")
        return False
    if role_id and user.role_id != role_id:
        return False

    g.user = user
    return True


# The authorize decorator
def authorize(role_id=None):
    """
    A decorator to protect routes and check if the user is authorized.

    Args:
        role_id (int | None): The role ID required to access the resource.
                              If None, any authenticated user can access.

    Returns:
        function: The decorated function, which will either be called if authorized
                  or return a 403 Forbidden response if not.
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not check_authorization(role_id):
                # If authorization fails, return a 403 Forbidden response
                return (
                    jsonify(
                        {
                            "error": "Forbidden",
                            "message": "You are not authorized to access this resource.",
                        }
                    ),
                    403,
                )
            return f(*args, **kwargs)  # Call the original function if authorized

        return decorated_function

    return decorator

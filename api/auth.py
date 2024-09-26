from functools import wraps
from flask import jsonify, session, g

from .database import User


# Simple example of a user authentication check function
def check_authorization():
    # In a real app, you'd verify the user session, token, or API key here
    # This is just a simple placeholder logic for demonstration
    print(session.get("user_id"))
    user = User.query.get(session.get("user_id"))
    print(user)
    if not user:
        print("GET HERE")
        return False
    g.user = user
    return True


# The authorize decorator
def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not check_authorization():
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

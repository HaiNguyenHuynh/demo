from flask import jsonify, Blueprint, request, session, g

from database.models import User, Profile, db
from auth import authorize

api_bp = Blueprint("views", __name__)


@api_bp.route("/users", methods=["GET"])
def get_user_list():
    try:
        users = User.query.all()
        user_list = [{"id": user.id, "email": user.email} for user in users]
        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        email = data.get("email")
        new_user = User(email=email)
        new_profile = Profile(user=new_user, bio="")

        db.session.add(new_user)
        db.session.add(new_profile)

        db.session.commit()

        return jsonify({"data": "OK"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        email = data.get("email")

        user = User.query.filter_by(email=email).first_or_404()
        session["user_id"] = user.id
        return jsonify({"data": "OK"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/register", methods=["POST"])
def register():
    return ({"data": "register OK"}), 200


@api_bp.route("/logout", methods=["POST"])
def logout():
    session.pop("user_id")
    return jsonify({"data": "OK"}), 200


@api_bp.route("/me", methods=["GET"])
@authorize
def get_own_profile():
    current_user = g.user
    return jsonify({"email": current_user.email}), 200

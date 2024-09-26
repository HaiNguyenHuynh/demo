from datetime import date
from flask import jsonify, Blueprint, request, session, g, render_template
from werkzeug.security import generate_password_hash, check_password_hash

from auth import authorize
from database.models import User, Profile, db
from services.user_services import (
    get_all_users,
    get_user_by_id,
    get_users_by_role,
)


ADMIN_ROLE_ID = 1


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
@authorize(ADMIN_ROLE_ID)
def create_user():
    DEFAULT_ROLE_ID = 2
    DEFAULT_DATE_OF_BIRTH = date(200, 1, 1)
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        hahsed_password = generate_password_hash(password)
        new_user = User(email=email, role_id=DEFAULT_ROLE_ID, password=hahsed_password)
        new_profile = Profile(user=new_user, bio="", first_name="", last_name="", date_of_birth=DEFAULT_DATE_OF_BIRTH)

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
        password = data.get("password")

        user = User.query.filter_by(email=email).first_or_404()

        if not check_password_hash(user.password, password):        
            return jsonify({"error": "Invalid email or password"}), 400

        session["user_id"] = user.id
        response = jsonify({"data": "OK"})
        response.set_cookie("role", str(user.role_id))
        return response, 200

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


@api_bp.route("/", defaults={"path": ""})
@api_bp.route("/<path:path>")
def index(path):
    return render_template("index.html")

from datetime import date
from flask import jsonify, Blueprint, redirect, request, session, g, render_template
from werkzeug.security import generate_password_hash, check_password_hash

from views.sso_routes import init_saml_auth, prepare_flask_request
from auth import authorize
from database.models import User, Profile, Role, db


ADMIN_ROLE_ID = 1


api_bp = Blueprint("views", __name__)


@api_bp.route("/users", methods=["GET"])
def get_user_list():
    try:
        users = User.query.all()
        user_list = [
            {"id": user.id, "email": user.email, "is_sso": user.is_sso}
            for user in users
        ]
        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/users", methods=["POST"])
@authorize(ADMIN_ROLE_ID)
def create_user():
    DEFAULT_ROLE_ID = 2
    DEFAULT_DATE_OF_BIRTH = date(2000, 1, 1)
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        hahsed_password = generate_password_hash(password)
        new_user = User(email=email, role_id=DEFAULT_ROLE_ID, password=hahsed_password)
        # new_profile = Profile(user=new_user, bio="", first_name="", last_name="", date_of_birth=DEFAULT_DATE_OF_BIRTH)

        db.session.add(new_user)
        # db.session.add(new_profile)

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
        role = Role.query.get(user.role_id)

        if not check_password_hash(user.password, password):
            return jsonify({"error": "Invalid email or password"}), 400

        session["user_id"] = user.id
        response = jsonify({"data": "OK"})
        response.set_cookie("role", role.name)
        return response, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/register", methods=["POST"])
def register():
    DEFAULT_ROLE_ID = 2
    DEFAULT_DATE_OF_BIRTH = date(2000, 1, 1)
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        hahsed_password = generate_password_hash(password)
        new_user = User(email=email, role_id=DEFAULT_ROLE_ID, password=hahsed_password)
        # new_profile = Profile(user=new_user, bio="", first_name="", last_name="", date_of_birth=DEFAULT_DATE_OF_BIRTH)

        db.session.add(new_user)
        # db.session.add(new_profile)

        db.session.commit()

        return jsonify({"data": "OK"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@api_bp.route("/logout", methods=["POST"])
def logout():
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
    current_user = g.user
    return jsonify({"email": current_user.email}), 200

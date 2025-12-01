from flask import Blueprint, request, jsonify
from user_db import add_user, log_in_user, update_user_timestamp

auth_blueprint = Blueprint("auth", __name__)


# New user sign up
@auth_blueprint.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()

        role = data.get("role")
        username = data.get("username")
        password = data.get("password")
        name = data.get("name")
        email = data.get("email")

        success = add_user(role, username, password, name, email)

        if not success:
            raise Exception("Failed to add user to database")

        return jsonify(
            {
                "success": True,
                "message": "Registration successful",
                "user": {
                    "role": role,
                    "username": username,
                    "name": name,
                    "email": email,
                },
            }
        ), 201
    except Exception as e:
        print(f"Registration unsuccessful: {e}")
        return jsonify({"success": False, "message": str(e)}), 400


# Logging in existing user
@auth_blueprint.route("/log_in", methods=["POST"])
def log_in():
    try:
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        success, user_id, role = log_in_user(username, password)

        if not success:
            raise Exception("Failed to log in user")

        # update timestamp whenever user logs in
        update_user_timestamp(user_id)

        return jsonify(
            {
                "success": True,
                "message": "Registration successful",
                "user": {
                    "id": user_id,
                    "role": role,
                    "username": username,
                },
            }
        ), 201
    except Exception as e:
        print(f"Login unsuccessful: {e}")
        return jsonify({"success": False, "message": str(e)}), 400

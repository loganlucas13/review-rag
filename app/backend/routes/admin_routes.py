from flask import Blueprint, request, jsonify
from user_db import get_all_users, edit_user

admin_blueprint = Blueprint("admin", __name__)


@admin_blueprint.route("/retrieve_registered_users", methods=["GET"])
def retrieve_registered_users():
    results = get_all_users()
    if results:
        return jsonify({"success": True, "users": results}), 200
    return jsonify({"success": False, "message": "Failed to retrieve users"}), 500


@admin_blueprint.route("/edit_profile/<int:user_id>", methods=["PUT"])
def edit_profile(user_id: int):
    data = request.get_json()

    role = data.get("role")
    username = data.get("username")
    password = data.get("password")
    name = data.get("name")
    email = data.get("email")

    if edit_user(user_id, role, username, password, name, email):
        return jsonify({"success": True}), 200
    return jsonify({"success": False, "message": "Failed to edit user"}), 500

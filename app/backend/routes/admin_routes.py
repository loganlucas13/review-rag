from flask import Blueprint, request, jsonify
from user_db import get_all_users, edit_user, remove_user

admin_blueprint = Blueprint("admin", __name__)


# Retrieves all registered users from the database
@admin_blueprint.route("/retrieve_registered_users", methods=["GET"])
def retrieve_registered_users():
    results = get_all_users()
    if results:
        return jsonify({"success": True, "users": results}), 200
    return jsonify({"success": False, "message": "Failed to retrieve users"}), 500


# Edits the profile with user_id with new values (from request body)
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


# Deletes the profile of a user with user_id
@admin_blueprint.route("/delete_profile/<int:user_id>", methods=["DELETE"])
def delete_profile(user_id: int):
    success = remove_user(user_id)
    if success:
        return jsonify({"success": True}), 200
    return jsonify({"success": False, "message": "Failed to delete user"}), 500

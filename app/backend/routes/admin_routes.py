from flask import Blueprint, jsonify
from user_db import get_all_users

admin_blueprint = Blueprint("admin", __name__)


@admin_blueprint.route("/retrieve_registered_users", methods=["GET"])
def retrieve_registered_users():
    results = get_all_users()
    if results:
        return jsonify({"success": True, "users": results}), 200
    else:
        return jsonify({"success": False, "message": "Failed to retrieve users"}), 500


@admin_blueprint.route("/edit_profile/<int:user_id>", methods=["PUT"])
def edit_profile(user_id: int):
    # allows the admin to modify the profile of user_id
    return True

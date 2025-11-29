from flask import Blueprint

admin_blueprint = Blueprint("admin", __name__)


@admin_blueprint.route("/retrieve_registered_users", methods=["GET"])
def retrieve_registered_users() -> None:
    # retrieves a list of all registered users
    return  # not sure what return type should be, maybe a list or json?


@admin_blueprint.route("/edit_profile/<int:user_id>", methods=["PUT"])
def edit_profile(user_id: int) -> bool:
    # allows the admin to modify the profile of user_id
    return True

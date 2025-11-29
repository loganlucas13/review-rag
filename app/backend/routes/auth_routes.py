from flask import Blueprint

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/register", methods=["POST"])
def register() -> bool:
    # new user sign up
    return True


@auth_blueprint.route("/log_in", methods=["POST"])
def log_in() -> bool:
    # user log in
    return True

from flask import Blueprint, request, jsonify

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/register", methods=["POST"])
def register() -> bool:
    # new user sign up
    try:
        data = request.get_json()

        role = data.get("role")
        username = data.get("username")
        password = data.get("password")
        name = data.get("name")
        email = data.get("email")

        # TODO: insert user information into User table

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


@auth_blueprint.route("/log_in", methods=["POST"])
def log_in() -> bool:
    # user log in
    return True

from flask import Blueprint

enduser_blueprint = Blueprint("enduser", __name__)


@enduser_blueprint.route("/submit_query", methods=["GET"])
def submit_query():
    # user submits a query and gets response
    # query passed in through request.args
    return ""

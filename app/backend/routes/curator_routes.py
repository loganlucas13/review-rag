from flask import Blueprint

curator_blueprint = Blueprint("curator", __name__)


@curator_blueprint.route("/upload_document", methods=["POST"])
def upload_document():
    # upload a document (passed in request files)
    # requirement 3: store all metadata correctly
    return True


@curator_blueprint.route("/delete_document/<int:document_id>", methods=["DELETE"])
def remove_document(document_id: int):
    # deletes document with `document_id`
    return True

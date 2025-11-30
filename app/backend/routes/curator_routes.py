from flask import Blueprint, request, jsonify
from document_db import get_documents, add_document, remove_document

curator_blueprint = Blueprint("curator", __name__)


@curator_blueprint.route("/get_documents", methods=["GET"])
def get_all_documents():
    results = get_documents()
    if results is not None:
        return jsonify({"success": True, "documents": results}), 200
    return jsonify({"success": False, "message": "Failed to retrieve documents"}), 500


@curator_blueprint.route("/upload_document", methods=["POST"])
def upload_document():
    data = request.get_json()

    filename = data.get("filename")
    media_type = data.get("media_type")
    file_data = data.get("file_data")
    added_by = data.get("added_by")

    success = add_document(filename, media_type, file_data, added_by)

    if success:
        return jsonify({"success": True}), 200
    return jsonify({"success": False, "message": "Failed to upload document"}), 500


@curator_blueprint.route("/delete_document/<int:document_id>", methods=["DELETE"])
def delete_document(document_id: int):
    success = remove_document(document_id)
    if success:
        return jsonify({"success": True}), 200
    return jsonify({"success": False, "message": "Failed to delete document"}), 500

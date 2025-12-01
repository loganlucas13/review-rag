from flask import Blueprint, request, jsonify
from querying import perform_query

enduser_blueprint = Blueprint("enduser", __name__)


# Submits a query for processing from an EndUser
# Returns top-5 most similar results (using both Cosine Similarity and Inner Product)
@enduser_blueprint.route("/submit_query", methods=["POST"])
def submit_query():
    try:
        data = request.json

        query = data.get("query")
        user_id = data.get("user_id")
        document_id = data.get("document_id")

        results = perform_query(query, user_id, document_id)

        if not results:
            raise Exception("Query unsuccessful")
        return jsonify(
            {
                "success": True,
                "query_id": results["query_id"],
                "results": results["results"],
            }
        ), 200
    except Exception as e:
        print(f"Query unsuccessful: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

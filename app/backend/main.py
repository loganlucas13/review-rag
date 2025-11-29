from flask import Flask
from flask_cors import CORS
from routes import auth_blueprint, admin_blueprint, curator_blueprint, enduser_blueprint

from postgres_login import login
from user_db import setup_user_db
from document_db import setup_document_db
from querylog_db import setup_querylog_db
from querylogdocument_db import setup_querylogdocument_db
from vector_db import setup_vector_db

# set up Flask app with CORS and register all endpoints
app = Flask(__name__)
CORS(app)
app.register_blueprint(auth_blueprint, url_prefix="/api/auth")
app.register_blueprint(admin_blueprint, url_prefix="/api/admin")
app.register_blueprint(curator_blueprint, url_prefix="/api/curator")
app.register_blueprint(enduser_blueprint, url_prefix="/api/enduser")


@app.route("/")
def api_home():
    return "API running...\n"


# calls all functions needed to get the API ready to take requests
def api_setup() -> bool:
    print("Logging into database...\n")
    cursor = login()
    if not cursor:
        raise Exception("Invalid cursor")

    print("Setting up User table...\n")
    if not setup_user_db(cursor):
        raise Exception("User table setup failed")

    print("Setting up Document table...\n")
    if not setup_document_db(cursor):
        raise Exception("Document table setup failed")

    print("Setting up QueryLog table...\n")
    if not setup_querylog_db(cursor):
        raise Exception("QueryLog table setup failed")

    print("Setting up QueryLogDocument table...\n")
    if not setup_querylogdocument_db(cursor):
        raise Exception("QueryLogDocument table setup failed")

    print("Setting up Vector database...\n")
    if not setup_vector_db(cursor):
        raise Exception("Vector database setup failed")


# Main program flow: runs automatically using Docker compose
if __name__ == "__main__":
    try:
        print("Setting up API...\n")
        api_setup()

        print("Starting Flask server...\n")
        app.run(host="0.0.0.0", port=4196, debug=True, use_reloader=False)
    except Exception as e:
        print(f"Error while setting up API: {str(e)}")
        raise

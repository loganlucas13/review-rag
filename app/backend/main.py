from flask import Flask
from routes import admin_blueprint, curator_blueprint, enduser_blueprint

# these will get moved into the api endpoints once we get the API implemented
from postgres_login import login
from chunking import wine_data_extraction, chunk_text
from vector_embedding import create_embeddings
from vector_db import db_setup, save_to_vector_database
from querying import inner_product, cosine_similarity

# set up Flask app and register all endpoints
app = Flask(__name__)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(curator_blueprint, url_prefix="/curator")
app.register_blueprint(enduser_blueprint, url_prefix="/enduser")


@app.route("/")
def api_home():
    return "API running...\n"


# Main program flow: runs automatically using Docker compose
if __name__ == "__main__":
    CSV_DATA_FILE = "data/wine-reviews/winemag-data.csv"

    try:
        print("Logging into database...\n")
        cursor = login()

        print("Setting up pgvector...\n")
        db_setup(cursor)

        print("Extracting Wine Data...\n")
        data = wine_data_extraction(CSV_DATA_FILE)

        print("Chunking Text Data...\n")
        chunked_data = chunk_text(data, max_words=25, overlap=5)

        print(f"Embedding {len(chunked_data)} chunks...\n")
        embeddings = create_embeddings(chunked_data)

        print("Saving embeddings into database...\n")
        save_to_vector_database(cursor, embeddings, chunked_data)

        print("Computing results with Cosine Similarity...\n")
        results = cosine_similarity(cursor, "Italian wine")
        for result in results:
            print(f"{result.get('id', '')}:")
            print(f"  {result.get('text', '')}")
            print(f"  {result.get('score', '')}")
            print(f"  {result.get('algorithm', '')}")
            print()

        print("Computing results with Inner Product...\n")
        results = inner_product(cursor, "Italian wine")
        for result in results:
            print(f"{result.get('id', '')}:")
            print(f"  {result.get('text', '')}")
            print(f"  {result.get('score', '')}")
            print(f"  {result.get('algorithm', '')}")
            print()
    except Exception as e:
        print(f"Error: {str(e)}")
        raise

    print("Starting Flask server...\n")
    app.run(host="0.0.0.0", port=4196, debug=True, use_reloader=False)

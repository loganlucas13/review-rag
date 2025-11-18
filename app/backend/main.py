from flask import Flask
import numpy as np
from postgres_login import login
from chunking import wine_data_extraction, chunk_text
from vector_embedding import create_embeddings
from vector_db import db_setup, save_to_vector_database

app = Flask(__name__)


@app.route("/")
def root_route():
    # Implementation for Flask API will be done in Phase 4
    print("start of route")
    return "Vector Database API Running"


if __name__ == "__main__":
    CSV_DATA_FILE = "app/backend/data/wine-reviews/winemag-data_first150k.csv"

    try:
        cursor = login()
        print("Logged into Database")

        db_setup(cursor)

        print("Extracting Wine Data")
        data = wine_data_extraction(CSV_DATA_FILE)
        print("Chunking Text Data")
        chunked_data = chunk_text(data)
        print(f"Embedding {len(chunked_data)} amount of chunks")
        embeddings = create_embeddings(chunked_data)
        print("Saving embedding into database")
        save_to_vector_database(cursor, embeddings, chunked_data)
        print("Data saved successfuly into database")

    except Exception as e:
        print(f"Error: {str(e)}")
        raise

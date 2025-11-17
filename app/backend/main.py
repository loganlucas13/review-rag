# starting point for database's Flask API
# note: not sure exactly where to go from here

from flask import Flask
import numpy as np
from postgres_login import login
from chunking import wine_data_extraction, chunk_text
from vector_embedding import create_embeddings

app = Flask(__name__)


@app.route("/")
def root_route():
    print("start of route")
    return


if __name__ == "__main__":
    CSV_DATA_FILE = "app/backend/data/wine-reviews/winemag-data_first150k.csv"

    cursor = login()
    data = wine_data_extraction(CSV_DATA_FILE)
    chunked_data = chunk_text(data)
    embeddings = create_embeddings(chunked_data)

    save_to_vector_database(cursor, embeddings, chunked_data)
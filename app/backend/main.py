# starting point for database's Flask API
# note: not sure exactly where to go from here

from flask import Flask
import numpy as np
from postgres_login import login
from chunking import wine_data_extraction, chunk_text
from vector_embedding import create_embeddings
from vector_db import save_to_vector_database
from pgvector.psycopg2 import register_vector

app = Flask(__name__)


@app.route("/")
def root_route():
    print("start of route")
    return "Vector Database API Running"


# Sets up database with pgvector extension and creates tables
def db_setup(cursor):
    cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")

    register_vector(cursor.connection)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vectors (
        id SERIAL PRIMARY KEY,
        chunk TEXT NOT NULL,
        embedding vector(384)
    );
    """)

    cursor.connection.commit()
    print("Vector Database Setup Successfully")


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

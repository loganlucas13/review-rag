# Storing emeddings into vector database
# Phase 3: Step 3

from typing import List
from pgvector.psycopg2 import register_vector
from psycopg2.extensions import cursor
import numpy as np
from tqdm import tqdm  # Progress bar


# Sets up database with pgvector extension and creates tables
def db_setup(cursor: cursor) -> None:
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


# Saves vector embeddings to vector database using pgvector
def save_to_vector_database(
    cursor: cursor,
    embeddings: np.ndarray,
    chunked_data: List[str],
    batch_size: int = 100,
) -> None:
    register_vector(cursor.connection)

    insert_table = """
    INSERT INTO Vectors (chunk, embedding) VALUES (%s, %s);
    """

    data_for_insert = []

    with tqdm(
        total=len(embeddings), desc="Saving to Database", unit="Vectors"
    ) as progressBar:
        for i in range(len(embeddings)):
            # Turns Numpy Array into a List
            embedding_list = (
                embeddings[i].tolist()
                if isinstance(embeddings[i], np.ndarray)
                else embeddings[i]
            )

            # Checking to see if Embedding has Right Dimensions
            if len(embedding_list) != 384:
                print(f"Embedding at {i} has dimension {len(embedding_list)}, Skipping")
                progressBar.update(1)
                continue

            data_for_insert.append((chunked_data[i], embedding_list))

            # Batch Insertion for Efficiency
            if len(data_for_insert) >= batch_size:
                cursor.executemany(insert_table, data_for_insert)
                cursor.connection.commit()
                print(f"Processed a batch of {len(data_for_insert)} records")
                progressBar.update(len(data_for_insert))
                data_for_insert = []

    # Inserts any Remaining Embeddings
    if data_for_insert:
        cursor.executemany(insert_table, data_for_insert)
        cursor.connection.commit()
        print(f"Inserted final batch of {len(data_for_insert)} records")
        progressBar.update(len(data_for_insert))

    print(f"Successfully saved {len(embeddings)} embeddings to the vector database")

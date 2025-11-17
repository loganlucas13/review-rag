import pgvector
from typing import List
import numpy as np
from pgvector.psycopg2 import register_vector
from postgres_login import login
from sentence_transformers import SentenceTransformer

def vector_embedding(chunks: List[str]) -> np.ndarray:
    model = SentenceTransformer("sentence_transformers/all-MiniLM-L6-v2")
    emb_matrix = model.encode(chunks, convert_to_numpy=True, normalize_embeddings=True, batch_size=32)

    return emb_matrix



def setup_pgvector(conn):
    register_vector(conn)

    pass


def create_embeddings():
    cursor = login()
    conn = cursor.connection

    register_vector(conn)


if __name__ == "__main__":
    create_embeddings()
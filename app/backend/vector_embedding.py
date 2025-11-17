# vector embedding
# phase 3 step 2
from pgvector.psycopg2 import register_vector
from postgres_login import login
import numpy as np


def setup_pgvector(conn):
    register_vector(conn)

    pass


def create_embeddings():
    cursor = login()
    conn = cursor.connection

    register_vector(conn)


if __name__ == "__main__":
    create_embeddings()

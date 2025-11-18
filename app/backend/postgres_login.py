import psycopg2
from psycopg2.extensions import cursor
import os
from dotenv import load_dotenv


# Login to postgres server using .env password
# Returns connection cursor
def login() -> cursor:
    load_dotenv()

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )
    return conn.cursor()

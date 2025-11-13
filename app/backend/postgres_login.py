import psycopg2
import os
from dotenv import load_dotenv


# login to postgres server using .env password
# returns connection cursor
def login():
    load_dotenv()

    print("logging in...")
    print("environment variables:")
    print(f"  {os.getenv('POSTGRES_HOST')}")
    print(f"  {os.getenv('POSTGRES_PORT')}")
    print(f"  {os.getenv('POSTGRES_DB')}")
    print(f"  {os.getenv('POSTGRES_USER')}")
    print(f"  {os.getenv('POSTGRES_PASSWORD')}")

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )
    return conn.cursor()


if __name__ == "__main__":
    print("testing postgres_login file...")
    cursor = login()
    print(f"successfully connected: {cursor}")

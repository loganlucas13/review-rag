from typing import List
from psycopg2.extensions import cursor


# Create 'User' table in database (if it doesn't exist)
# Returns True if successful, False otherwise
def setup_user_db(cursor: cursor) -> bool:
    try:
        create_user_table_query = """
            CREATE TABLE IF NOT EXISTS "User" (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                role VARCHAR(7) NOT NULL CHECK(role IN ('EndUser', 'Admin', 'Curator')),
                username VARCHAR(20) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                last_activity_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(create_user_table_query)
        return True
    except Exception as e:
        print(f"Error while creating User table: {e}")
        return False


# Add a user to the user database
def add_user() -> bool:
    return True


# Remove a user from the user database
def remove_user() -> bool:
    return True


# return a given user's information (as json?)
def get_user() -> dict:
    return {}

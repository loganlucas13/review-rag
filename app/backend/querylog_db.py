from typing import List
from psycopg2.extensions import cursor


# Creates 'QueryLog' table (if it doesn't exist)
# Returns True if successful, False otherwise
def setup_querylog_db(cursor: cursor) -> bool:
    try:
        create_querylog_table_query = """
            CREATE TABLE IF NOT EXISTS "QueryLog" (
                query_id SERIAL PRIMARY KEY,
                id INT NOT NULL,
                text VARCHAR(255) NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id) REFERENCES "User"(id)
            );
        """
        cursor.execute(create_querylog_table_query)
        return True
    except Exception as e:
        print(f"Error while creating QueryLog database: {e}")
        return False


# Adds a QueryLog whenever a query is made
def add_query_log():
    # TODO: for 3.3
    return True


# Removes all querylogs from a specific user
def remove_user_querylogs(user_id: int):
    # TODO
    return True

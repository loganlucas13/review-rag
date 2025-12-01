from typing import List
from psycopg2.extensions import cursor
from postgres_login import login


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
def add_query_log(text: str, user_id: int) -> int:
    try:
        add_querylog_query = """
            INSERT INTO "QueryLog" (id, text)
            values (%s, %s)
            RETURNING query_id;
        """
        cursor = login()
        cursor.execute(add_querylog_query, (user_id, text))
        query_id = cursor.fetchone()[0]
        cursor.close()
        return query_id
    except Exception as e:
        print(f"Error while adding query log: {e}")
        return -1


# Removes all querylogs from a specific user
def remove_user_querylogs(user_id: int) -> bool:
    try:
        get_query_ids_query = """
            SELECT query_id
            FROM "QueryLog"
            WHERE id = %s;
        """

        delete_query_ids_query = """
            DELETE FROM "QueryLogDocument"
            WHERE query_id = ANY(%s);
        """

        delete_query_logs_query = """
            DELETE FROM "QueryLog"
            WHERE query_id = ANY(%s);
        """

        cursor = login()
        cursor.execute(get_query_ids_query, (user_id,))
        query_ids = cursor.fetchall()
        query_ids = [
            row[0] for row in query_ids
        ]  # get first element of every response tuple

        if not query_ids:
            return True

        cursor.execute(delete_query_ids_query, (query_ids,))
        cursor.execute(delete_query_logs_query, (query_ids,))
        cursor.close()
        return True
    except Exception as e:
        print(f"Error while removing user query logs: {e}")
        return False

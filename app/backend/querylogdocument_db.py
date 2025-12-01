from typing import List
from psycopg2.extensions import cursor
from postgres_login import login


# Creates 'QueryLogDocument' table (if it doesn't exist)
# Returns True if successful, False otherwise
def setup_querylogdocument_db(cursor: cursor) -> bool:
    try:
        create_querylogdocument_table_query = """
            CREATE TABLE IF NOT EXISTS "QueryLogDocument" (
                query_id INT,
                document_id INT,
                PRIMARY KEY (query_id, document_id),
                FOREIGN KEY (query_id) REFERENCES "QueryLog"(query_id),
                FOREIGN KEY (document_id) REFERENCES "Document"(document_id)
            );
        """
        cursor.execute(create_querylogdocument_table_query)
        return True
    except Exception as e:
        print(f"Error while creating QueryLogDocument table: {e}")
        return False


# Add an entry to the 'QueryLogDocument' table
def add_querylogdocument_entry(query_id: int, document_id: int) -> bool:
    try:
        add_entry_query = """
            INSERT INTO "QueryLogDocument" (query_id, document_id)
            VALUES (%s, %s);
        """

        cursor = login()
        cursor.execute(add_entry_query, (query_id, document_id))
        cursor.close()
        return True
    except Exception as e:
        print(f"Error while adding QueryLogDocument entry: {e}")
        return False


# Removes an entry from the 'QueryLogDocument' table with the given document_id
def remove_querylogdocument_entry(document_id: int) -> bool:
    try:
        remove_entry_query = """
            DELETE FROM "QueryLogDocument"
            WHERE document_id = %s
        """

        cursor = login()
        cursor.execute(remove_entry_query, (document_id,))
        cursor.close()
        return True
    except Exception as e:
        print(f"Error while removing QueryLogDocument entry: {e}")
        return False

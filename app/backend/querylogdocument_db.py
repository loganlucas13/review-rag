from typing import List
from psycopg2.extensions import cursor


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

from typing import List
from psycopg2.extensions import cursor


# Creates 'Document' table (if it doesn't exist)
# Returns True if successful, False otherwise
def setup_document_db(cursor: cursor) -> bool:
    try:
        create_document_table_query = """
            CREATE TABLE IF NOT EXISTS "Document" (
                document_id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                type VARCHAR(50),
                source VARCHAR(50),
                added_by INT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                has_been_processed BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (added_by) REFERENCES "User"(id)
            );
        """
        cursor.execute(create_document_table_query)
        return True
    except Exception as e:
        print(f"Error while creating Document table: {e}")
        return False

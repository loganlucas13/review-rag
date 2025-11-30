import base64
import os
from typing import List
from psycopg2.extensions import cursor
from postgres_login import login
from chunking import chunk_text, wine_data_extraction
from vector_embedding import create_embeddings
from vector_db import save_to_vector_database

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


def get_documents() -> List[dict]:
    try:
        get_documents_query = """
            SELECT document_id, title, type, source, added_by, timestamp, has_been_processed
            FROM "Document"
            ORDER BY document_id;
        """

        cursor = login()
        cursor.execute(get_documents_query)
        results = cursor.fetchall()
        cursor.close()

        documents = []
        for result in results:
            documents.append(
                {
                    "id": result[0],
                    "title": result[1],
                    "type": result[2],
                    "source": result[3],
                    "added_by": result[4],
                    "timestamp": str(result[5]) if result[5] else None,
                    "has_been_processed": result[6],
                }
            )
        return documents
    except Exception as e:
        print(f"Error while logging in user: {e}")
        return []


def add_document(filename, media_type, file_data, added_by) -> bool:
    try:
        file_contents = base64.b64decode(file_data)

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join("uploads", filename)
        with open(file_path, "wb") as file:
            file.write(file_contents)

        #chunking/vectors/embeddings
        file = wine_data_extraction(file_path)
        chunks = chunk_text(file)
        embeddings = create_embeddings(chunks)

        add_document_query = """
            INSERT INTO "Document" (title, type, source, added_by, has_been_processed)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING document_id;
        """

        cursor = login()

        cursor.execute(
            add_document_query, (filename, media_type, file_path, added_by, False)
        )
        document_id = cursor.fetchone()[0]
        save_to_vector_database(cursor, document_id, embeddings, chunks)
        cursor.close()
        return True
    except Exception as e:
        print(f"Error while adding document: {e}")
        return False


# Removes document with 'document_id'
def remove_document(document_id: int) -> bool:
    try:
        get_path_query = """
            SELECT source
            FROM "Document"
            WHERE document_id = %s;
        """

        cursor = login()
        cursor.execute(get_path_query, (document_id,))
        file_path = cursor.fetchone()[0]

        remove_document_query = """
            DELETE FROM "Document"
            WHERE document_id = %s;
        """

        cursor.execute(remove_document_query, (document_id,))
        cursor.close()

        # remove file from 'uploads' folder
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
        return True
    except Exception as e:
        print(f"Error while removing document: {e}")
        return False

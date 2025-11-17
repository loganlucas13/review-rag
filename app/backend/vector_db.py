# Storing emeddings into vector database
# Phase 3: Step 3

## TODO: Initialize pgvector so that the create_table query actually works
## (right now, if you try to run you get an error saying "psycopg2.errors.UndefinedObject: type "vector" does not exist")

# Saves vector embeddings to vector database using pgvector
def save_to_vector_database(curr, embeddings, chunked_data):
    create_table = """
    CREATE TABLE IF NOT EXISTS Vectors (
        id SERIAL PRIMARY KEY,
        chunk TEXT NOT NULL,
        embedding vector(384)
    );
    """
    insert_table = """
    INSERT INTO Vectors (chunk, embedding) VALUES (%s, %s);
    """

    curr.execute(create_table)
    for i in range(len(embeddings)):
        curr.execute(insert_table, (chunked_data[i], embeddings[i]))

    curr.commit()

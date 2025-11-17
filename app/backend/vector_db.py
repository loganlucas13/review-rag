# Storing emeddings into vector database
# Phase 3: Step 3

# Saves vector embeddings to vector database using pgvector
def save_to_vector_database(curr, embeddings, chunked_data):
    create_table = """
    CREATE TABLE IF NOT EXISTS vectors (
        id SERIAL PRIMARY KEY,
        chunk TEXT NOT NULL,
        embedding vector(50)
    );
    """
    insert_table = """
    INSERT INTO vectors (chunk, embedding) VALUES (%s, %s);
    """

    curr.execute(create_table)
    for i in range(len(embeddings)):
        curr.execute(insert_table, (chunked_data[i], embeddings[i]))

    curr.commit()
    return
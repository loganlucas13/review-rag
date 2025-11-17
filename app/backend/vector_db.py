# Storing emeddings into vector database
# Phase 3: Step 3

## TODO: Initialize pgvector so that the create_table query actually works
## (right now, if you try to run you get an error saying "psycopg2.errors.UndefinedObject: type "vector" does not exist")

# Saves vector embeddings to vector database using pgvector
from pgvector.psycopg2 import register_vector
import numpy as np
from tqdm import tqdm

def save_to_vector_database(curr, embeddings, chunked_data, batch_size=100):
    
    register_vector(curr.connection)

    insert_table = """
    INSERT INTO Vectors (chunk, embedding) VALUES (%s, %s);
    """

    data_for_insert = []

    with tqdm(total = len(embeddings), desc="Saving to Database", unit="Vectors") as progressBar:
        for i in range(len(embeddings)):

            # Turns Numpy Array into a List
            embedding_list = embeddings[i].tolist() if isinstance(embeddings[i], np.ndarray) else embedding[i]

            # Checking to see if Embedding has Right Dimensions
            if len(embedding_list) != 384:
                print(f"Embedding at {i} has dimension {len(embedding_list)}, Skipping")
                progressBar.update(1)
                continue

            data_for_insert.append((chunked_data[i], embedding_list))

            # Batch Insertion for Efficiency
            if len(data_for_insert) >= batch_size:
                curr.executemany(insert_table, data_for_insert)
                curr.connection.commit()
                print(f"Processed a batch of {len(data_for_insert)} records")
                progressBar.update(len(data_for_insert))
                data_for_insert = []

    # Inserts any Remaining Embeddings
    if data_for_insert:
        curr.executemany(insert_table, data_for_insert)
        curr.connection.commit()
        print(f"Inserted final batch of {len(data_for_insert)} records")
        progressBar.update(len(data_for_insert))
    

    print(f"Successfully saved {len(embeddings)} embeddings to the vector database")
# CS 480 Group Project

### Group Name: popeyes

## Phase 3 Requirements

1. Step 1: Chunking:
    - Located in `app/backend/chunking.py`.
    - `chunk_text()`
2. Step 2: Chunks -> Vectors:
    - Located in `app/backend/vector_embedding.py`.
    - `create_embeddings()`
3. Step 3: Vector -> VectorDB:
    - Located in `app/backend/vector_db.py`.
    - `save_to_vector_database()`
4. Step 4: Query Answering:
    - Located in `app/backend/querying.py`.
    - `inner_product()` and `cosine_similarity()`

## Setup

> [!IMPORTANT]
> Make sure to have Docker installed.

1. Add your environment variables to a new file named `.env` in the root directory.
    - Required variable names are in the `sample.env` file.
2. Run the command `docker compose up --build` in the terminal from the root directory of this project.
3. ?

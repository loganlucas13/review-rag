# Backend

> [!WARNING]
> WIP

-   Uses [Flask](https://flask.palletsprojects.com/en/stable/).

## Phase 3 Requirements

> [!NOTE]
> All helper functions are called in `app/backend/main.py`.

### Step 1: Chunking:

-   Located in `app/backend/chunking.py`.
-   `chunk_text()`

### Step 2: Chunks -> Vectors:

-   Located in `app/backend/vector_embedding.py`.
-   `create_embeddings()`

### Step 3: Vector -> VectorDB:

-   Located in `app/backend/vector_db.py`.
-   `save_to_vector_database()`

### Step 4: Query Answering:

-   Located in `app/backend/querying.py`.
-   `inner_product()` and `cosine_similarity()`

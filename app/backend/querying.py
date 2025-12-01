# Query answering
# Phase 3: Step 4

from typing import List
from psycopg2.extensions import cursor
from postgres_login import login
from vector_embedding import create_embeddings
from querylog_db import add_query_log
from querylogdocument_db import add_querylogdocument_entry


# Inner Product/Dot Product
# scores between -inf to inf, higher is more similar
def inner_product(
    cursor: cursor, query: str, document_id: int, k: int = 5
) -> List[int]:
    query_embedding = create_embeddings([query])[0]

    # <#> is negative inner product, multiply by -1 to get actual inner product
    sql_query = """
        SELECT id, chunk,
               (embedding <#> %s::vector) * -1 AS dot_product
        FROM "Vectors"
        WHERE document_id = %s
        ORDER BY embedding <#> %s::vector
        LIMIT %s;
    """
    cursor.execute(
        sql_query, (query_embedding.tolist(), document_id, query_embedding.tolist(), k)
    )

    results = cursor.fetchall()
    return format_results(results, "inner_product")


# Cosine Similarity: scores between -1 to 1, 1 being most similar
def cosine_similarity(
    cursor: cursor, query: str, document_id: int, k: int = 5
) -> List[int]:
    query_embedding = create_embeddings([query])[0]

    # <=> is cosine distance
    sql_query = """
        SELECT id, chunk,
               1 - (embedding <=> %s::vector) AS cosine_similarity
        FROM "Vectors"
        WHERE document_id = %s
        ORDER BY embedding <=> %s::vector
        LIMIT %s;
    """
    cursor.execute(
        sql_query, (query_embedding.tolist(), document_id, query_embedding.tolist(), k)
    )

    results = cursor.fetchall()
    return format_results(results, "cosine_similarity")


# Formats results into a list of dicts
def format_results(results: List[str], algorithm_name: str) -> List[dict]:
    formatted = []
    for row in results:
        formatted.append(
            {
                "id": row[0],
                "text": row[1],
                "score": float(row[2]),
                "algorithm": algorithm_name,
            }
        )
    return formatted


# Performs similarity tests on the given 'query' parameter and returns results
def perform_query(query: str, user_id: int, document_id: int) -> dict:
    try:
        query_id = add_query_log(query, user_id)
        if query_id == -1:
            raise Exception("Error while adding QueryLog entry")

        success = add_querylogdocument_entry(query_id, document_id)
        if not success:
            raise Exception("Error while adding QueryLogDocument entry")

        cursor = login()

        cosine_similarity_results = cosine_similarity(cursor, query, document_id, k=5)
        inner_product_results = inner_product(cursor, query, document_id, k=5)

        return {
            "query_id": query_id,
            "results": {
                "cosine_similarity": cosine_similarity_results,
                "inner_product": inner_product_results,
            },
        }
    except Exception as e:
        print(f"Error while performing query: {e}")
        return {}

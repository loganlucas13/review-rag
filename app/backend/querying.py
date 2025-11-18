# Query answering
# Phase 3: Step 4

from typing import List
from vector_embedding import create_embeddings
from psycopg2.extensions import cursor


# Inner Product/Dot Product
# scores between -inf to inf, higher is more similar
def inner_product(cursor: cursor, query: str, k: int = 5) -> List[int]:
    query_embedding = create_embeddings([query])[0]

    # <#> is negative inner product, multiply by -1 to get actual inner product
    sql_query = """
        SELECT id, chunk,
               (embedding <#> %s::vector) * -1 AS dot_product
        FROM Vectors
        ORDER BY embedding <#> %s::vector
        LIMIT %s;
    """
    cursor.execute(sql_query, (query_embedding.tolist(), query_embedding.tolist(), k))

    results = cursor.fetchall()
    return format_results(results, "inner_product")


# Cosine Similarity: scores between -1 to 1, 1 being most similar
def cosine_similarity(cursor: cursor, query: str, k: int = 5) -> List[int]:
    query_embedding = create_embeddings([query])[0]

    # <=> is cosine distance
    sql_query = """
        SELECT id, chunk,
               1 - (embedding <=> %s::vector) AS cosine_similarity
        FROM Vectors
        ORDER BY embedding <=> %s::vector
        LIMIT %s;
    """
    cursor.execute(sql_query, (query_embedding.tolist(), query_embedding.tolist(), k))

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

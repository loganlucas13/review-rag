# Query answering
# Phase 3: Step 4

from typing import List
from vector_embedding import create_embeddings
import psycopg2


# change the k for k nearest neighbors

# Inner Product: also called dot product
# scores between -inf to inf, higher is more similar
def inner_product(curr, query, k: int = 5) -> List[int]:
    print("in inner product")
    query_embedding = create_embeddings([query])[0]
    print("query embedded")

    # <#> is negative inner product, multiply by -1 to get actual inner product
    sql_query = """
        SELECT id, chunk,
               (embedding <#> %s::vector) * -1 AS dot_product
        FROM Vectors
        ORDER BY embedding <#> %s::vector
        LIMIT %s;
    """
    print("executing query")
    curr.execute(sql_query, (query_embedding.tolist(), query_embedding.tolist(), k))

    print("executed query")
    results = curr.fetchall()
    print("fetched results")
    return format_results(results, "inner_product")

# Cosine Similarity: scores between -1 to 1, 1 being most similar
def cosine_similarity(curr, query, k: int = 5) -> List[int]:
    query_embedding = create_embeddings([query])[0]

    # <=> is cosine distance
    sql_query = """
        SELECT id, chunk,
               1 - (embedding <=> %s::vector) AS cosine_similarity
        FROM Vectors
        ORDER BY embedding <=> %s::vector
        LIMIT %s;
    """
    curr.execute(sql_query, (query_embedding.tolist(), query_embedding.tolist(), k))

    results = curr.fetchall()
    return format_results(results, "cosine_similarity")

def format_results(results, algorithm_name):
    print("formatting results")
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
    print("results formatted")
    return formatted

# Query answering
# Phase 3: Step 4

from typing import List
from vector_embedding import create_embeddings
import psycopg2


# change the k for k nearest neighbors
def inner_product(curr, query, k: int = 5) -> List[int]:
    print("in inner product")
    query_embedding = create_embeddings([query])[0]
    print("query embedded")

    # <#> is negative inner product, multiply by -1 to get actual inner product
    query = """
        SELECT id, chunk,
               (embedding <#> %s::vector) * -1 AS dot_product
        FROM Vectors
        ORDER BY embedding <#> %s::vector
        LIMIT %s;
    """
    print("executing query")
    curr.execute(query, (query_embedding.tolist(), query_embedding.tolist(), k))

    print("executed query")
    results = curr.fetchall()
    print("fetched results")
    return format_results(results, "inner_product")


def cosine_similarity(curr, query, k: int = 5) -> List[int]:
    pass


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

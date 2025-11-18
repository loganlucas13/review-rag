# Query answering
# Phase 3: Step 4

from typing import List
from vector_embedding import create_embeddings
import psycopg2

#change the k for k nearest neighbors
def inner_product(curr, query, k: int = 5) -> List[int]:
    query_embedding = create_embeddings([query])[0]
    
    # <#> is negative inner product, multiply by -1 to get actual inner product
    query = """
        SELECT id, chunk,
               (embedding <#> %s::vector) * -1 AS dot_product
        FROM Vectors
        ORDER BY embedding <#> %s::vector
        LIMIT %s;
    """
    curr.execute(query, (query_embedding.tolist(), query_embedding.tolist(), k))
    
    results = curr.fetchall()
    return format_results(results, "inner_product")

def cosine_similarity(curr, query, k: int = 5) -> List[int]:
    pass

def format_results(results, algorithm_name):
    formatted = []
    for row in results:
        formatted.append({
            "id": row[0],
            "text": row[1],
            "score": float(row[2]),
            "algorithm": algorithm_name
        })
    return formatted
# Creating vector embeddings
# Phase 3: Step 2

from typing import List
import numpy as np
from fastembed import TextEmbedding


# Creates vector embeddings from chunks using the fastembed library
def create_embeddings(chunks: List[str]) -> np.ndarray:
    embedded_chunks = list(
        TextEmbedding(model_name="BAAI/bge-small-en-v1.5").embed(chunks)
    )
    embeddings = np.array(embedded_chunks)
    return embeddings

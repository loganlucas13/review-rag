# vector embedding
# phase 3 step 2
import pgvector
from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

def vector_embedding(chunks: List[str]) -> np.ndarray:
    model = SentenceTransformer("sentence_transformers/all-MiniLM-L6-v2")
    emb_matrix = model.encode(chunks, convert_to_numpy=True, normalize_embeddings=True, batch_size=32)

    return emb_matrix




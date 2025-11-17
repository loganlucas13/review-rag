from typing import List
import numpy as np
from fastembed import TextEmbedding


def create_embeddings(chunks: List[str]) -> np.ndarray:
    print(f"starting embedding for {len(chunks)} chunks...")
    embedded_chunks = list(
        TextEmbedding(model_name="BAAI/bge-small-en-v1.5").embed(chunks)
    )
    embeddings = np.array(embedded_chunks)
    print("embedding done")
    return embeddings


if __name__ == "__main__":
    text = ""
    embeddings = create_embeddings(text)
    print(embeddings)

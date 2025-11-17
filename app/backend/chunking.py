# chunking text
# phase 3 step 1

import numpy as np
from typing import List


def chunk_text(text: str, max_words: int = 200, overlap: int = 40) -> List[str]:
    words = text.split()
    chunks = []

    i = 0
    while i < len(words):
        chunk = words[i : i + max_words]
        if not chunk:
            break
        chunks.append(" ".join(chunk))
        i += max_words - overlap
    return chunks


if __name__ == "__main__":
    chunks = chunk_text()

import numpy as np
from sentence_transformers import SentenceTransformer # for text -> vector embedding
import faiss # an example of a vector DB (currently stores in the memory)


def chunk_text(text, max_words=200, overlap=40):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+max_words]
        if not chunk:
            break
        chunks.append(" ".join(chunk))
        i += max_words - overlap  # slide window with overlap
    return chunks

chunks = chunk_text(jiopjopjipjopjiopjipjopjiopjiojioop, max_words=20, overlap=10)
print(f"Total chunks: {len(chunks)}")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")  # 384-dim
emb_matrix = model.encode(chunks, convert_to_numpy=True, normalize_embeddings=True)

dim = emb_matrix.shape[1]
index = faiss.IndexFlatIP(dim)  # cosine works with normalized vectors using inner product
index.add(emb_matrix)           # store embeddings


def search(query, k=3):
    q_emb = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    scores, idxs = index.search(q_emb, k)  # (1, k)
    results = []
    for rank, (i, s) in enumerate(zip(idxs[0], scores[0]), start=1):
        results.append({"rank": rank, "score": float(s), "chunk": chunks[i]})
    return results

query = "awjeiefoajwoipfaewjfoieawjofaewifjeawfeawfjaewfaejwofewafewafaewfoiaewfwafoafewawofejafaewoifjweaeogjaweiopghaweiofjiwoeapghiawojgwhneifpoajwengoiwajefhnaopwe;fjawieopfjaiwofjwioefjawiofjawieofjaewoifjawefiopawjefioajwfiopewjafioawef"

hits = search(query, k=3)

print("\nTop matches:")
for h in hits:
    print(f"[{h['rank']}] score={h['score']:.3f}\n{h['chunk']}\n---")
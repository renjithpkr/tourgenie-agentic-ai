import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Example Data (Artists & Events)
texts = [
    "Theyyam is a ritualistic dance form of Kerala",
    "Kathakali is a traditional storytelling dance of Kerala",
    "Kannur is famous for Theyyam performances"
]

# Convert Texts to Embeddings
embeddings = embedding_model.encode(texts)

# Convert to FAISS-compatible format
embeddings = np.array(embeddings).astype('float32')

# Create a FAISS Index (L2 Distance Search)
dimension = 384  # Embedding size
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)  # Store the vectors in FAISS

print("FAISS index built with", index.ntotal, "entries")


# New Query
query = "Tell me about Kerala's traditional dance forms"

# Convert Query to Embedding
query_embedding = embedding_model.encode([query]).astype('float32')

# Search FAISS for 2 Nearest Neighbors
_, indices = index.search(query_embedding, k=2)

# Retrieve Matched Entries
retrieved_results = [texts[i] for i in indices[0]]

print("Query:", query)
print("Top Matches:", retrieved_results)

from sentence_transformers import SentenceTransformer

# Load Pre-trained Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Example Data
texts = [
    "Theyyam is a ritualistic dance form of Kerala",
    "Kathakali is a traditional storytelling dance of Kerala",
    "Kannur is famous for Theyyam performances"
]

# Convert Text to Embeddings
embeddings = embedding_model.encode(texts)

print(embeddings.shape)  # Output: (3, 384) -> 3 texts, each with a 384-dimensional vector
print(embeddings[0])  # First text's vector representation

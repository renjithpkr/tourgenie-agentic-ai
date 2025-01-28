import torch
from langchain.llms import LlamaCpp
from sentence_transformers import SentenceTransformer
import faiss

# Verify PyTorch
print("Torch Version:", torch.__version__)

# Verify LangChain LLM
try:
    llm = LlamaCpp(model_path="C:\Projects\ExploreMalabarAgents\llama-2-7b.Q3_K_S.gguf", n_ctx=2048)
    print("LlamaCpp Loaded Successfully!")
except Exception as e:
    print("LlamaCpp Error:", e)

# Verify Sentence Transformers
try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("Sentence Transformer Loaded Successfully!")
except Exception as e:
    print("Sentence Transformer Error:", e)

# Verify FAISS
try:
    dimension = 384  # Match embedding size
    index = faiss.IndexFlatL2(dimension)
    print("FAISS Initialized Successfully!")
except Exception as e:
    print("FAISS Error:", e)

from fastapi import FastAPI, HTTPException, Body
from sqlalchemy import create_engine, Column, Integer, String, Text, Table, MetaData
from sqlalchemy.orm import sessionmaker
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import LlamaCpp
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

app = FastAPI()

# Database Configuration
#DATABASE_URL = "postgresql://postgres:123123@localhost:5432/malabar_db"
DATABASE_URL = os.getenv("DATABASE_URL")#"postgresql://postgres:123123@db:5432/malabar_db"
MODEL_PATH = os.getenv("MODEL_PATH")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()

# Define Tables
artists = Table(
    'artists', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('bio', Text),
    Column('category', String),
    Column('location', String)
)

cultural_events = Table(
    'cultural_events', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('description', Text),
    Column('date', String),
    Column('location', String)
)

# Load AI Model
llm = LlamaCpp(model_path=MODEL_PATH, n_ctx=2048, temperature=0.7)

# Initialize Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize FAISS Index
dimension = 384  # Embedding size
index = faiss.IndexFlatL2(dimension)

# Function to Load Data from DB and Create Embeddings
def load_data_into_vector_db():
    session = SessionLocal()
    data_points = []
    
    artist_data = session.execute(artists.select()).fetchall()
    event_data = session.execute(cultural_events.select()).fetchall()
    session.close()

    for a in artist_data:
        data_points.append(f"Artist: {a[1]}, Bio: {a[2]}, Location: {a[4]}")
    
    for e in event_data:
        data_points.append(f"Event: {e[1]}, Description: {e[2]}, Date: {e[3]}, Location: {e[4]}")

    embeddings = np.array(embedding_model.encode(data_points))
    index.add(embeddings)
    return data_points

# Load Data into FAISS
data_store = load_data_into_vector_db()

# AI Query Function
def agentic_ai(question: str):
    query_embedding = np.array(embedding_model.encode([question]))
    _, indices = index.search(query_embedding, k=2)
    retrieved_data = [data_store[i] for i in indices[0]]
    
    context = "\n".join(retrieved_data)
    response = llm(f"Use the following knowledge: {context}\nAnswer: {question}")
    return response

# Query API Endpoint
@app.post("/query")
async def ai_query(question: str = Body(..., embed=True)):
    try:
        response = agentic_ai(question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health Check API
@app.get("/health")
async def health_check():
    return {"status": "Healthy"}

# Analytics API
@app.get("/analytics")
async def analytics():
    return {"message": "Returning analytics data"}

# Use an official Python runtime as base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -U langchain-community

# Set environment variables for database and model path
ENV DATABASE_URL="postgresql://postgres:123123@172.18.0.2:5435/malabar_db"
ENV MODEL_PATH="/models/llama-2-7b.Q3_K_S.gguf"

# Ensure the /models directory exists inside the container
RUN mkdir -p /models

# Expose API port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "exploreapiwithvolume:app", "--host", "0.0.0.0", "--port", "8000"]

import chromadb
from chromadb.config import Settings

# Use the existing persistent database
client = chromadb.HttpClient(
    settings=Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="D:/New folder1"  # Old PC path
    ),
    host="0.0.0.0",  # Listen on all interfaces
    port=8000       # Default port
)
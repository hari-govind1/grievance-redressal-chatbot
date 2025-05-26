from embedding import model
from vector_store import VectorStore
import config

def search_query(query, vector_store):
    """Finds the most relevant text chunks based on a query."""
    query_embedding = model.encode(query)
    results = vector_store.search(query_embedding, top_k=config.TOP_K)
    return " ".join(results)



# #for chromadb
# from embedding import generate_embeddings
# from vector_store import VectorStore

# def search_query(query, vector_store, top_k=5):
#     query_embedding = generate_embeddings([query])[0]  # Generate query embedding
#     results = vector_store.search(query_embedding, top_k)
#     return " ".join(results)  # Combine retrieved texts

import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension):
        """Initializes FAISS vector database."""
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []

    def add_documents(self, chunks, embeddings):
        """Adds document embeddings to FAISS index."""
        np_embeddings = np.array(embeddings).astype('float32')
        self.index.add(np_embeddings)
        self.chunks = chunks  # Store text chunks for retrieval

    def search(self, query_embedding, top_k=3):
        """Searches the FAISS index for the closest vectors."""
        query_embedding = np.array([query_embedding]).astype('float32')
        _, indices = self.index.search(query_embedding, top_k)
        return [self.chunks[i] for i in indices[0]]




# #for chromadb
# import chromadb

# class VectorStore:
#     def __init__(self, collection_name="college_rules"):
#         self.client = chromadb.PersistentClient(path="./chroma_db")  # Persistent storage
#         self.collection = self.client.get_or_create_collection(collection_name)

#     def add_documents(self, texts, embeddings):
#         for i, (text, embedding) in enumerate(zip(texts, embeddings)):
#             self.collection.add(
#                 ids=[str(i)],
#                 embeddings=[embedding],
#                 metadatas=[{"text": text}]
#             )

#     def search(self, query_embedding, top_k=5):
#         results = self.collection.query(
#             query_embeddings=[query_embedding], 
#             n_results=top_k
#         )
#         return [item["text"] for item in results["metadatas"]]

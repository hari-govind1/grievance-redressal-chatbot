import chromadb

print("Starting...")
client = chromadb.PersistentClient(path="D:/New folder1")
print("Client initialized.")
collection = client.get_collection('grievance_data')
print("Collection loaded.")
try:
    print("Fetching embeddings...")
    results = collection.get(include=["embeddings"])
    print("Embeddings fetched:", results['embeddings'][:5])
except Exception as e:
    print(f"Embedding error: {str(e)}")
print("Done.")
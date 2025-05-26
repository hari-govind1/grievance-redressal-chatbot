import chromadb
#from chromadb.config import Settings
#this prohram is to retrieve datas from the chroms databse
# Initialize Chroma DB client
client = chromadb.PersistentClient(path="D:/New folder1")

# Load the collection
#collection_name = "my_collection"  # Replace with your collection name
collection = client.get_collection('grievance_data')

# Fetch all inserted documents, embeddings, and metadata
results = collection.get(
    include=["documents", "metadatas", "embeddings"]
)

# Display the results
for i, doc in enumerate(results["documents"]):
    print(f"Document {i}: {doc}")
    print(f"Metadata {i}: {results['metadatas'][i]}")
    print(f"Embedding {i} (first 5 values): {results['embeddings'][i][:5]}")
    print("-" * 50)
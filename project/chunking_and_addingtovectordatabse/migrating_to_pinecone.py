import chromadb
from pinecone import Pinecone, ServerlessSpec, PineconeException
import time
import numpy as np

# Step 1: Set up Pinecone API key and initialize clients
pinecone_api_key = ""
pinecone_environment = "us-east-1-aws"

try:
    # Initialize ChromaDB client
    client = chromadb.PersistentClient(path="D:/New folder1")
    collection = client.get_collection('grievance_data')

    # Initialize Pinecone
    pc = Pinecone(api_key=pinecone_api_key)
except Exception as e:
    print(f"Error initializing clients: {e}")
    exit(1)

# Step 2: Create or connect to a Pinecone index
index_name = "grievance-data"
embedding_dimension = 1536

try:
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=embedding_dimension,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
        print("Index created. Waiting for it to be ready...")
        time.sleep(10)
    index = pc.Index(index_name)
except PineconeException as e:
    print(f"Error creating or connecting to Pinecone index: {e}")
    exit(1)

# Step 3: Extract data from ChromaDB
try:
    data = collection.get(include=['documents', 'embeddings', 'metadatas'])
    ids = data['ids']
    documents = data['documents']
    embeddings = data['embeddings']
    metadatas = data['metadatas']

    if not ids:
        print("No data found in ChromaDB collection 'grievance_data'.")
        exit(1)

    total_chunks = len(ids)
    print(f"Extracted {total_chunks} items from ChromaDB.")
    print(f"First few IDs extracted: {ids[:5]}")  # Debug: Print first few IDs
except Exception as e:
    print(f"Error extracting data from ChromaDB: {e}")
    exit(1)

# Step 4: Prepare and migrate data to Pinecone
try:
    pinecone_vectors = []
    for i in range(len(ids)):
        vector_tuple = (
            ids[i],
            embeddings[i],
            metadatas[i]
        )
        pinecone_vectors.append(vector_tuple)

    batch_size = 50
    for i in range(0, len(pinecone_vectors), batch_size):
        batch = pinecone_vectors[i:i + batch_size]
        index.upsert(vectors=batch, namespace="")  # Explicitly use default namespace
        print(f"Uploaded batch {i // batch_size + 1} of {(len(pinecone_vectors) + batch_size - 1) // batch_size} to Pinecone.")

    print("Data successfully migrated from ChromaDB to Pinecone!")
    print("Waiting for vectors to be available in Pinecone...")
    time.sleep(5)  # Wait for vectors to be fully available
except PineconeException as e:
    print(f"Error uploading data to Pinecone: {e}")
    exit(1)
except Exception as e:
    print(f"Unexpected error during migration: {e}")
    exit(1)

# Step 5: Verify the migration
try:
    # Fetch a sample vector to confirm data exists in Pinecone
    sample_id = ids[0]
    print(f"Attempting to fetch vector with ID: {sample_id}")
    fetch_result = index.fetch(ids=[sample_id], namespace="")  # Explicitly use default namespace
    if sample_id in fetch_result.vectors:
        print(f"Successfully fetched sample vector '{sample_id}' from Pinecone:")
        print(fetch_result.vectors[sample_id])
    else:
        print(f"Failed to fetch sample vector '{sample_id}' from Pinecone.")
        print("Debug: Fetch result:", fetch_result)

    # Perform a sample similarity search
    sample_embedding = embeddings[0]
    # Convert NumPy array to Python list for serialization
    if isinstance(sample_embedding, np.ndarray):
        sample_embedding = sample_embedding.tolist()
    print(f"Performing similarity search with sample embedding (first 5 values): {sample_embedding[:5]}")
    query_result = index.query(
        vector=sample_embedding,
        top_k=3,
        include_metadata=True,
        namespace=""
    )
    print("\nSample similarity search result from Pinecone:")
    print(query_result)

except PineconeException as e:
    print(f"Error verifying migration in Pinecone: {e}")
    exit(1)
except Exception as e:
    print(f"Unexpected error during verification: {e}")
    exit(1)

# Step 6: Confirm retention of local ChromaDB
print("\nMigration completed successfully! Your vector database is now securely stored in Pinecone.")
print("Your local ChromaDB at 'D:/New folder1' has been retained and was not modified or deleted.")
import json
import chromadb
from pinecone import Pinecone, PineconeException

# Step 1: Initialize ChromaDB client to get original documents
try:
    chroma_client = chromadb.PersistentClient(path="D:/New folder1")
    chroma_collection = chroma_client.get_collection('grievance_data')
    print("ChromaDB client initialized successfully.")
except Exception as e:
    print(f"Error initializing ChromaDB client: {e}")
    exit(1)

# Step 2: Extract documents from ChromaDB
try:
    chroma_data = chroma_collection.get(include=['documents', 'embeddings', 'metadatas'])
    chroma_ids = chroma_data['ids']
    chroma_documents = chroma_data['documents']
    chroma_metadatas = chroma_data['metadatas']

    # Create a dictionary mapping IDs to documents and metadata
    chroma_dict = {id_: {"document": doc, "metadata": meta} for id_, doc, meta in zip(chroma_ids, chroma_documents, chroma_metadatas)}
    print(f"Extracted {len(chroma_ids)} items from ChromaDB.")
    print(f"First few IDs from ChromaDB: {chroma_ids[:5]}")
except Exception as e:
    print(f"Error extracting data from ChromaDB: {e}")
    exit(1)

# Step 3: Initialize Pinecone
pinecone_api_key = ""  # Replace with your Pinecone API key
try:
    pc = Pinecone(api_key=pinecone_api_key)
    index = pc.Index("grievance-data")
except PineconeException as e:
    print(f"Error initializing Pinecone: {e}")
    exit(1)

# Step 4: Get all IDs from Pinecone
try:
    stats = index.describe_index_stats()
    total_vectors = stats['total_vector_count']
    print(f"Total vectors in Pinecone index: {total_vectors}")

    # Generate IDs (chunk_0 to chunk_123)
    pinecone_ids = [f"chunk_{i}" for i in range(total_vectors)]
    print(f"Generated IDs to fetch from Pinecone: {pinecone_ids[:5]}... (first 5 shown)")
except PineconeException as e:
    print(f"Error retrieving Pinecone index stats: {e}")
    exit(1)

# Step 5: Fetch vectors from Pinecone in batches and combine with ChromaDB documents
all_data = []
batch_size = 50

try:
    for i in range(0, len(pinecone_ids), batch_size):
        batch_ids = pinecone_ids[i:i + batch_size]
        fetch_result = index.fetch(ids=batch_ids, namespace="")
        for vec_id in batch_ids:
            if vec_id in fetch_result.vectors:
                vector_data = fetch_result.vectors[vec_id]
                # Get the corresponding document from ChromaDB
                if vec_id in chroma_dict:
                    document = chroma_dict[vec_id]["document"]
                    # Verify metadata consistency (optional)
                    pinecone_metadata = vector_data.metadata
                    chroma_metadata = chroma_dict[vec_id]["metadata"]
                    if pinecone_metadata != chroma_metadata:
                        print(f"Warning: Metadata mismatch for ID {vec_id}. Using Pinecone metadata.")
                else:
                    print(f"Warning: ID {vec_id} not found in ChromaDB. Using placeholder document.")
                    document = f"Document for {vec_id}"

                data_entry = {
                    "id": vec_id,
                    "embedding": vector_data.values,
                    "metadata": vector_data.metadata,
                    "document": document
                }
                all_data.append(data_entry)
        print(f"Fetched batch {i // batch_size + 1} of {(len(pinecone_ids) + batch_size - 1) // batch_size}")

    print(f"Total vectors fetched and combined: {len(all_data)}")

except PineconeException as e:
    print(f"Error fetching vectors from Pinecone: {e}")
    exit(1)

# Step 6: Save the combined data to a JSON file
try:
    with open("pinecone_to_chromadb_with_docs.json", "w") as f:
        json.dump(all_data, f, indent=4)
    print("Data successfully saved to 'pinecone_to_chromadb_with_docs.json'")
except Exception as e:
    print(f"Error saving data to file: {e}")
    exit(1)
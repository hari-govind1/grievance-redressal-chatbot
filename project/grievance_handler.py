# grievance_handler.py
import openai
import chromadb
import openaiAPIkey

# Set your OpenAI API key
openAi_key = openaiAPIkey.open_ai_api_key
openai.api_key = openAi_key

# Initialize Chroma client
client = chromadb.PersistentClient(path="D:/New folder1")

# Create a collection in Chroma
collection = client.get_collection('grievance_data')

# Function to get embeddings from OpenAI
def get_embeddings(text: str):
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=text
    )
    return response['data'][0]['embedding']

# Function to query the ChromaDB with a text and retrieve similar documents
def query_chroma(query_text: str, top_k=10):
    departments = []
    query_embedding = get_embeddings(query_text)
    if query_embedding is None:
        return

    try:
        # Perform the search
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        # Collect and return department IDs
        for i, result in enumerate(results['documents'][0]):  # Access the first query's results
            metadata = results['metadatas'][0][i]  # Access metadata for the current result
            department_id = metadata.get('department_id', 'N/A')
            departments.append(department_id)
        return departments
    except Exception as e:
        print(f"Error querying Chroma DB: {e}")

# This function will be called from another program to handle grievance input
def handle_grievance(grievance_text: str):
    top_ten_departments = query_chroma(grievance_text)

    # Creating dictionary with all departments with a default value of 0
    keys = ['Academic department', 'Administrative department', 'Hostel Department', 'Library Department', 
            'Cafeteria Department', 'Placement Department', 'Technical Support Department', 'Transportation Department', 
            'Electrical Maintenance Department']
    default_value = 0

    top_ten_departments_count = dict.fromkeys(keys, default_value)

    # Count how many times each department appears in the top results
    for dept in top_ten_departments:
        top_ten_departments_count[dept] += 1

    # Sort the department counts in descending order
    top_ten_departments_count_desc = dict(sorted(top_ten_departments_count.items(), key=lambda item: item[1], reverse=True))

    iterator = iter(top_ten_departments_count_desc.items())
    first_key, first_value = next(iterator)
    second_key, second_value = next(iterator)

    # Return the most relevant department(s) for the grievance
    if first_value > second_value:
        predicted_department = first_key

    if first_value == second_value:
        predicted_department = [first_key, second_key]
    return predicted_department

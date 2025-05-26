import openai
import chromadb
import os
import openaiAPIkey

# Set your OpenAI API key
openAi_key= openaiAPIkey.open_ai_api_key
#initialising the open ai key 
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
    departments=[]
    query_embedding = get_embeddings(query_text)
    if query_embedding is None:
        return

    try:
        # Perform the search
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        # Print the department IDs and the corresponding texts of the results
        for i, result in enumerate(results['documents'][0]):  # Access the first query's results
            metadata = results['metadatas'][0][i]  # Access metadata for the current result
            department_id = metadata.get('department_id', 'N/A')  # Use .get() to handle missing keys
            departments.append(department_id)
            #print(f"Result {i + 1}: Department ID: {department_id}")#add , Grievance: {result} along with the department_id if we want the entire grievance
        return departments
    except Exception as e:
        print(f"Error querying Chroma DB: {e}")

# Example query
print("enter the grievance that you have with college(only one grievance at a time)")
query_text = input()
top_ten_departments=query_chroma(query_text)


#creating dictionary with sll the departement with default value as 0
keys = ['Academic department','Administrative department','Hostel Department','Library Department','Cafeteria Department','Placement Department','Technical Support Department','Transportation Department','Electrical Maintenance Department']
default_value = 0

top_ten_departments_count = dict.fromkeys(keys, default_value)

for i in top_ten_departments:
    top_ten_departments_count[i] += 1

top_ten_departments_count_desc = dict(sorted(top_ten_departments_count.items(), key=lambda item: item[1], reverse=True))

print(top_ten_departments_count_desc)

iterator = iter(top_ten_departments_count_desc.items())
first_key, first_value = next(iterator)
second_key, second_value = next(iterator)

if(first_value > second_value):#the top similar department
    print("Grievance department is:",first_key)

if(first_value == second_value): # the grievance may be related to both departments
    print(f"The grievance may be fits or second department: {first_key} or {second_key}")


print(top_ten_departments)
import openai
import openaiAPIkey
import grievance_handler
import database_handler
from pdf_processing import extract_text_from_pdf, split_text_into_chunks
from embedding import generate_embeddings
from vector_store import VectorStore
from search import search_query
from llm import generate_response


# Load OpenAI API key
openai.api_key = openaiAPIkey.open_ai_api_key  

# List of departments for classification
DEPARTMENTS = [
    "Academic Department", "Administrative Department", "Hostel Department",
    "Library Department", "Cafeteria Department", "Placement Department",
    "Technical Support Department", "Transportation Department", "Electrical Maintenance Department"
]

#this function helps to get the user details
def get_user_details():
    """Collects user details for grievance submission."""
    valid_classes = {"1st year", "2nd year", "3rd year", "4th year"}
    valid_departments = {"AI", "CSE", "MECH", "EEE", "ECE", "IT", "Artificial Intelligence", "Computer Science", "Mechanical Engineering", "Electrical and Electronics Engineering", "Electronics and Communication Engineering", "Information Technology"}
    
    attempts = 0
    while attempts < 2:
        name = input("Enter your name: ").strip()
        user_class = input("Enter your class (1st year, 2nd year, etc.): ").strip()
        user_department = input("Enter your department (short/full form): ").strip()
        location = input("Where did the grievance occur? ").strip()
        email = input("Enter your college email: ").strip()
        additional_comments = input("Additional comments (optional): ").strip()
        
        if user_class not in valid_classes:
            print("⚠️ Invalid class. Please enter a valid class (1st year, 2nd year, 3rd year, or 4th year).")
        elif user_department not in valid_departments:
            print("⚠️ Invalid department. Please enter a valid department.")
        elif not email.endswith("@karpagamtech.ac.in"):
            print("⚠️ Invalid email. Please enter a valid college email.")
        else:
            return name, user_class, user_department, location, email, additional_comments
        
        attempts += 1
        print("Please enter valid details. Attempts remaining:", 2 - attempts)
    
    print("Too many incorrect attempts. Exiting.")
    exit()

#this function checks whether the user entered details are legintimate or not
def verify_legitimacy(name, user_class, user_department, grievance_text, location):
    """Verify if the grievance details are legitimate using ChatGPT."""
    prompt = f"""
    Verify if the following grievance details are legitimate. Ensure the name is valid, 
    class and department are valid. Respond only with:
    - 'Legitimate' (if valid)
    - 'Not Legitimate' (if invalid)

    Name: {name}
    Class: {user_class}
    Department: {user_department}
    Grievance: {grievance_text}
    Location: {location}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5
    )

    return response["choices"][0]["message"]["content"].strip()


def is_meaningful_grievance(grievance_text):
    """Uses GPT-4o Mini to check if the grievance is meaningful."""
    prompt = f"""
    Determine if the following grievance is meaningful and relevant to a college grievance redressal system.
    Respond only with:
    - 'Valid' (if the grievance is meaningful)
    - 'Invalid' (if it is gibberish, irrelevant, or too vague)

    Grievance: "{grievance_text}"
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You check whether grievances are meaningful for a college redressal system."},
            {"role": "user", "content": prompt.strip()}
        ],
        max_tokens=5  # Ensures a short response
    )
    
    return response["choices"][0]["message"]["content"].strip()

def classify_with_openai(grievance_text, assigned_departments):
    """Uses GPT-4o Mini to verify grievance classification against a fixed department list."""
    prompt = f"""
    A grievance has been classified into a department. Your task is to verify if the classification is correct. 
    Choose only from the given department list. Respond strictly in this format:
    'Correct: Yes' (if correct) OR 'Correct: No, Suggested Department: [Department Name]'.

    Grievance: "{grievance_text}"
    Assigned Departments: "{', '.join(assigned_departments)}"
    Choose from: {", ".join(DEPARTMENTS)}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You are an AI that verifies grievance classification using a fixed department list."},
            {"role": "user", "content": prompt.strip()}
        ],
        max_tokens=15  # Keeps response short
    )
    
    return response["choices"][0]["message"]["content"]

def main():
    """Main program loop for grievance redressal."""
    PDF_PATH = """D:\Chat-Bot-Project-main\data\KIT Rules and regulation.pdf"""

    # Extract text from PDF
    text = extract_text_from_pdf(PDF_PATH)

    # Split text into chunks
    chunks = split_text_into_chunks(text)

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Initialize and store in FAISS
    vector_store = VectorStore(dimension=len(embeddings[0]))
    vector_store.add_documents(chunks, embeddings)
    print("Hi! Welcome to the Grievance Redressal Bot")
    
    while True:  # Loop to allow multiple grievances
        print("\nWhat do you want to do?")
        print("1. Press 1 for Q&A Bot")
        print("2. Press 2 for Grievance Redressal")
        print("3. Press 3 to Exit")
        
        choice = input("Enter your choice: ").strip()

        if(choice == "1"):
            while True:
                query = input("\nAsk a question (or type 'exit' to quit): ").strip()

                if query.lower() == "exit":
                    print("Exiting chatbot. Goodbye!")
                    break  # Stop execution

                if query:  # Proceed only if input is not empty
                    retrieved_text = search_query(query, vector_store)
                    answer = generate_response(query, retrieved_text)
                    print("\nChatbot Answer:\n", answer)
                else:
                    print("Please enter a valid question.")
        
        if choice == "3":
            print("Thank you for using the Grievance Redressal Bot. Goodbye! 👋")
            break  # Exit the loop
        
        elif choice == "2":
            attempts = 0  # To track the number of retries

            while True:
                print("Enter your grievance:")
                grievance_text = input().strip()

                # Step 1: Validate the grievance for meaningfulness
                validation_result = is_meaningful_grievance(grievance_text)
                if validation_result == "Valid":
                    break
                else:
                    print("⚠️ Invalid grievance. Please enter a meaningful grievance.")
            
            while attempts < 2:  # Allow only 2 retries for refining grievance
                # Step 2: Use local model to classify grievance
                assigned_departments = grievance_handler.handle_grievance(grievance_text)  # Returns a list

                # Step 3: Verify classification using GPT-4o Mini
                verification_result = classify_with_openai(grievance_text, assigned_departments)
                
                suggested_department = None
                if "Correct: No" in verification_result:
                    suggested_department = verification_result.split("Suggested Department:")[-1].strip()
                
                if isinstance(assigned_departments, str):
                    assigned_list = [dept.strip() for dept in assigned_departments.split(",")]
                elif isinstance(assigned_departments, list):  
                    assigned_list = [dept.strip() for dept in assigned_departments]
                else:
                    assigned_list = []  # Fallback if unexpected type
                assigned_list = [dept for dept in assigned_list if dept]  # Remove empty entries

                if suggested_department and suggested_department in assigned_list:
                    final_department = [suggested_department]
                    verification_result = "Correct: Yes"
                else:
                    final_department = assigned_list  # Default to assigned departments

                if "Correct: No" in verification_result:
                    attempts += 1
                    if attempts < 2:
                        print("The grievance lacks details. Please provide more details about your grievance:")
                        grievance_text = input().strip()
                        validation_result = is_meaningful_grievance(grievance_text)
                        if validation_result != "Valid":
                            print("⚠️ Invalid grievance. Please enter a more detailed grievance.")
                            continue
                    else:
                        final_department = [suggested_department] if suggested_department else assigned_list
                        break
                else:
                    break  # Exit loop if classification is correct

            # Display results if we want to do
            print("\n🔹 **Grievance Classification Result** 🔹")
            print(f"🏢 Final Department Assigned: {', '.join(final_department)}")

            # Ask the user if they want to submit another grievance
            # Collect user details
            name, user_class, user_department, location, email, additional_comments = get_user_details()
            print("The details of the user are as follows:", name, "\t", user_class, "\t", location, "\t", email, "\t", additional_comments)

            
            # Verify legitimacy
            legitimacy = verify_legitimacy(name, user_class, user_department, grievance_text, location)
            if legitimacy != "Legitimate":
                print("⚠️ Grievance details are not legitimate. Exiting.")
                exit()

            summary_prompt = f"Summarize the following grievance in 20 words or less:\n\nGrievance: {grievance_text}"
            summary_response = openai.ChatCompletion.create(
                model="gpt-4o-mini-2024-07-18",
                messages=[{"role": "user", "content": summary_prompt}],
                max_tokens=20  # Ensuring the summary is within the required length
            )
            summary = summary_response["choices"][0]["message"]["content"].strip()
            for department in final_department:
                database_handler.store_grievance(
                    department, name, user_class, user_department, location, email, summary, additional_comments
                )

            print("\n✅ Grievance submitted successfully and stored in the database.")
            
            while True:
                another = input("\nDo you want to submit another grievance? (yes/no): ").strip().lower()
                if another == "yes":
                    break  # Restart the grievance process
                elif another == "no":
                    print("Thank you for using the Grievance Redressal Bot. Have a great day! 🎉")
                    return  # Exit the function
                else:
                    print("⚠️ Invalid choice. Please type 'yes' or 'no'.")
        


if __name__ == "__main__":
    main()

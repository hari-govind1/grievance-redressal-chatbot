from flask import Flask, render_template, request, redirect, url_for, session
import openai
import openaiAPIkey
import grievance_handler
import database_handler
from pdf_processing import extract_text_from_pdf, split_text_into_chunks
from embedding import generate_embeddings
from vector_store import VectorStore
from search import search_query
from llm import generate_response
from flask_session import Session
import tracking_number_generator
from email_module import send_email 
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with a secure key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "harigovind",
    "database": "solved_grievances"  # Assuming you want to check resolved grievances
}

# Load OpenAI API key
openai.api_key = openaiAPIkey.open_ai_api_key  

# List of departments for classification
DEPARTMENTS = [
    "Academic Department", "Administrative Department", "Hostel Department",
    "Library Department", "Cafeteria Department", "Placement Department",
    "Technical Support Department", "Transportation Department", "Electrical Maintenance Department"
]

# Valid classes and departments for validation
VALID_CLASSES = {"1st year", "2nd year", "3rd year", "4th year"}
VALID_DEPARTMENTS = {
    "AI", "CSE", "MECH", "EEE", "ECE", "IT", 
    "Artificial Intelligence", "Computer Science", "Mechanical Engineering", 
    "Electrical and Electronics Engineering", "Electronics and Communication Engineering", 
    "Information Technology"
}

# PDF processing setup (done once at startup)
PDF_PATH = r"D:\Chat-Bot-Project-main\data\KIT Rules and regulation.pdf"
try:
    text = extract_text_from_pdf(PDF_PATH)
    chunks = split_text_into_chunks(text)
    embeddings = generate_embeddings(chunks)
    vector_store = VectorStore(dimension=len(embeddings[0]))
    vector_store.add_documents(chunks, embeddings)
except Exception as e:
    print(f"Error initializing PDF processing: {e}")
    raise

# Helper functions
def verify_legitimacy(name, user_class, user_department, grievance_text, location):
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
        max_tokens=5
    )
    return response["choices"][0]["message"]["content"].strip()

def classify_with_openai(grievance_text, assigned_departments):
    prompt = f"""
    A grievance has been classified into a department. Your task is to verify if the classification is correct. 
    Choose only from the given department list. Respond strictly in this format:
    'Correct: Yes' (if correct) OR 'Correct: No, Suggested Department: [Department Name]'.

    Grievance: "{grievance_text}"
    Assigned Departments: "{', '.join(assigned_departments)}"
    Choose from: {", ".join(DEPARTMENTS)}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": "You are an AI that verifies grievance classification using a fixed department list."},
                {"role": "user", "content": prompt.strip()}
            ],
            max_tokens=15
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error in classify_with_openai: {e}")
        return "Correct: No, Suggested Department: Academic Department"  # Fallback

# Routes
@app.route('/')
def home():
    session.clear()
    return render_template('index.html')

@app.route('/qa', methods=['GET', 'POST'])
def qa_bot():
    if 'qa_chat' not in session:
        session['qa_chat'] = [{"role": "bot", "message": "Hi! Ask me anything (or type 'exit' to return)."}]
    
    if request.method == 'POST':
        query = request.form.get('message', '').strip()
        if query.lower() == 'exit':
            session.pop('qa_chat', None)
            return redirect(url_for('home'))
        if query:
            session['qa_chat'].append({"role": "user", "message": query})
            retrieved_text = search_query(query, vector_store)
            answer = generate_response(query, retrieved_text)
            session['qa_chat'].append({"role": "bot", "message": answer})
            session.modified = True
        else:
            session['qa_chat'].append({"role": "bot", "message": "Please enter a valid question."})
            session.modified = True
    return render_template('qa.html', chat=session['qa_chat'])

@app.route('/grievance', methods=['GET', 'POST'])
def grievance():
    tracking_number = tracking_number_generator.generate_unique_tracking_number()
    print(f"Generated unique tracking number: {tracking_number}")
    if 'grievance_chat' not in session:
        session['grievance_chat'] = [{"role": "bot", "message": "Please tell me your grievance."}]
        session['step'] = 'grievance_text'
        session['data'] = {}
        session['attempts'] = 0  # Track classification attempts

    if request.method == 'POST':
        message = request.form.get('message', '').strip()
        chat = session['grievance_chat']
        step = session['step']
        data = session['data']
        attempts = session['attempts']

        print(f"Current step: {step}, Message: {message}")  # Debug

        if step == 'grievance_text':
            validation_result = is_meaningful_grievance(message)
            print(f"Grievance validation: {validation_result}")  # Debug
            if validation_result == 'Valid':
                chat.append({"role": "user", "message": message})
                chat.append({"role": "bot", "message": "Thanks! What's your name?"})
                data['grievance_text'] = message
                session['step'] = 'name'
            else:
                chat.append({"role": "user", "message": message})
                chat.append({"role": "bot", "message": "That doesn't seem meaningful. Please provide a valid grievance."})
        
        elif step == 'name':
            chat.append({"role": "user", "message": message})
            chat.append({"role": "bot", "message": "Which class are you in (e.g., 1st year, 2nd year)?"})
            data['name'] = message
            session['step'] = 'user_class'
        
        elif step == 'user_class':
            if message in VALID_CLASSES:
                chat.append({"role": "user", "message": message})
                chat.append({"role": "bot", "message": "What's your department (e.g., CSE, MECH)?"})
                data['user_class'] = message
                session['step'] = 'user_department'
            else:
                chat.append({"role": "user", "message": message})
                chat.append({"role": "bot", "message": "Invalid class. Please enter 1st year, 2nd year, 3rd year, or 4th year."})
        
        elif step == 'user_department':
            if message in VALID_DEPARTMENTS:
                chat.append({"role": "user", "message": message})
                chat.append({"role": "bot", "message": "Where did this grievance occur?"})
                data['user_department'] = message
                session['step'] = 'location'
            else:
                chat.append({"role": "user", "message": message})
                chat.append({"role": "bot", "message": "Invalid department. Please enter a valid one (e.g., CSE, AI)."})
        
        elif step == 'location':
            chat.append({"role": "user", "message": message})
            chat.append({"role": "bot", "message": "What's your college email?"})
            data['location'] = message
            session['step'] = 'email'
        
        elif step == 'email':
            if message.endswith("@karpagamtech.ac.in"):
                chat.append({"role": "user", "message": message})
                chat.append({"role": "bot", "message": "Any additional comments? (Type 'none' if none)"})
                data['email'] = message
                session['step'] = 'additional_comments'
            else:
                chat.append({"role": "user", "message": message})
                chat.append({"role": "bot", "message": "Invalid email. Please use your @karpagamtech.ac.in email."})
        
        elif step == 'additional_comments':
            chat.append({"role": "user", "message": message})
            data['additional_comments'] = message if message.lower() != 'none' else ''
            
            # Verify legitimacy
            legitimacy = verify_legitimacy(data['name'], data['user_class'], data['user_department'], 
                                        data['grievance_text'], data['location'])
            print(f"Legitimacy check: {legitimacy}")  # Debug
            if legitimacy != "Legitimate":
                chat.append({"role": "bot", "message": "Sorry, the details don't seem legitimate. Let's start over."})
                session.pop('grievance_chat', None)
                session.pop('step', None)
                session.pop('data', None)
                session.pop('attempts', None)
                return redirect(url_for('grievance'))

            # Classify grievance
            while attempts < 2:
                assigned_departments = grievance_handler.handle_grievance(data['grievance_text'])
                print(f"Assigned departments: {assigned_departments}")  # Debug
                verification_result = classify_with_openai(data['grievance_text'], assigned_departments)
                print(f"Verification result: {verification_result}")  # Debug
                suggested_department = None
                if "Correct: No" in verification_result:
                    suggested_department = verification_result.split("Suggested Department:")[-1].strip()
                
                # Ensure assigned_departments is handled correctly
                if isinstance(assigned_departments, (list, tuple)):
                    assigned_list = [dept.strip() for dept in assigned_departments if dept and isinstance(dept, str)]
                else:
                    assigned_list = [str(assigned_departments).strip()] if assigned_departments and isinstance(assigned_departments, str) else []
                
                # Use the assigned department if valid, or fall back to suggested_department
                final_department = []
                if assigned_list and any(dept in DEPARTMENTS for dept in assigned_list):
                    final_department = [dept for dept in assigned_list if dept in DEPARTMENTS]
                elif suggested_department and suggested_department in DEPARTMENTS:
                    final_department = [suggested_department]
                
                print(f"Final department after classification: {final_department}")  # Debug
                if not final_department and attempts < 2:
                    attempts += 1
                    session['attempts'] = attempts
                    chat.append({"role": "bot", "message": "The grievance lacks details. Please refine it."})
                    session['step'] = 'grievance_text'
                    continue
                elif not final_department:
                    chat.append({"role": "bot", "message": "Could not assign a valid department. Let's start over."})
                    session.pop('grievance_chat', None)
                    session.pop('step', None)
                    session.pop('data', None)
                    session.pop('attempts', None)
                    return redirect(url_for('grievance'))
                break  # Exit loop if we have a valid department

            if final_department:  # Proceed only if we have a valid department
                if 'final_department' not in data:
                    # Summarize grievance
                    try:
                        summary_prompt = f"Summarize the following grievance in 20 words or less:\n\nGrievance: {data['grievance_text']}"
                        summary_response = openai.ChatCompletion.create(
                            model="gpt-4o-mini-2024-07-18",
                            messages=[{"role": "user", "content": summary_prompt}],
                            max_tokens=20
                        )
                        summary = summary_response["choices"][0]["message"]["content"].strip()
                        print(f"Grievance summary: {summary}")  # Debug
                    except Exception as e:
                        chat.append({"role": "bot", "message": f"Error summarizing grievance: {str(e)}. Let's start over."})
                        session.pop('grievance_chat', None)
                        session.pop('step', None)
                        session.pop('data', None)
                        session.pop('attempts', None)
                        return redirect(url_for('grievance'))

                    # Store in database with validation
                    valid_departments = []
                    for department in final_department:
                        if department and isinstance(department, str) and department.strip() in DEPARTMENTS:
                            try:
                                print(f"Attempting to store grievance in '{department}'")  # Debug
                                database_handler.store_grievance(
                                    department, tracking_number, data['name'], data['user_class'], data['user_department'], 
                                    data['location'], data['email'], data['additional_comments'], summary
                                )
                                valid_departments.append(department)
                                print(f"Successfully stored in '{department}'")  # Debug
                            except Exception as e:
                                chat.append({"role": "bot", "message": f"Error storing grievance for '{department}': {str(e)}"})
                                print(f"Error storing grievance: {e}")  # Debug
                        else:
                            chat.append({"role": "bot", "message": f"Skipping invalid department: '{department}'"})
                            print(f"Skipped invalid department: '{department}'")  # Debug

                    '''if valid_departments:
                        send_email(data['email'], tracking_number, summary)
                        chat.append({"role": "bot", "message": f"Your grievance has been submitted successfully. Your tracking number is: {tracking_number}"})
                        chat.append({"role": "bot", "message": f"Would you like to submit another ? (yes/no)"})
                        session['step'] = 'another'
                        data['final_department'] = valid_departments'''
                    if valid_departments:
                        send_email(data['email'], tracking_number, summary)
                        # Simplified message without departments
                        chat.append({"role": "bot", "message": f"Grievance submitted successfully! Tracking: {tracking_number}. Would you like to submit another grievance? (yes/no)"})
                        session['step'] = 'another'
                        data['final_department'] = valid_departments
                    
                    else:
                        chat.append({"role": "bot", "message": "No valid departments assigned. Let's start over."})
                        session.pop('grievance_chat', None)
                        session.pop('step', None)
                        session.pop('data', None)
                        session.pop('attempts', None)
                        return redirect(url_for('grievance'))
        
        elif step == 'another':
            chat.append({"role": "user", "message": message})
            if message.lower() == 'yes':
                session.pop('grievance_chat', None)
                session.pop('step', None)
                session.pop('data', None)
                session.pop('attempts', None)
                return redirect(url_for('grievance'))
            elif message.lower() == 'no':
                chat.append({"role": "bot", "message": "Thanks for using the bot! Goodbye!"})
                session.pop('grievance_chat', None)
                session.pop('step', None)
                session.pop('data', None)
                session.pop('attempts', None)
                return redirect(url_for('home'))
            else:
                chat.append({"role": "bot", "message": "Please type 'yes' or 'no'."})

        session['grievance_chat'] = chat
        session['data'] = data
        session.modified = True

    return render_template('grievance.html', chat=session['grievance_chat'])
'''
@app.route('/track_grievance', methods=['GET', 'POST'])
def track_grievance():
    result = None
    if request.method == 'POST':
        tracking_number = request.form.get('tracking_number')

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM grievances WHERE tracking_number = %s", (tracking_number,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            result = {"error": f"Database error: {e}"}

    return render_template('track_grievance.html', result=result)
'''
@app.route('/track_grievance', methods=['GET', 'POST'])
def track_grievance():
    result = None
    message = None  # To store a message for unresolved grievances

    if request.method == 'POST':
        tracking_number = request.form.get('tracking_number')

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM grievances WHERE tracking_number = %s", (tracking_number,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            if not result:
                message = "Your grievance is still pending or does not exist in the resolved grievances database."
                
        except mysql.connector.Error as e:
            message = f"Database error: {e}"

    return render_template('track_grievance.html', result=result, message=message)


if __name__ == '__main__':
    print("Starting Flask Grievance Redressal Bot...")
    app.run(debug=True)
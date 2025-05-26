from flask import Flask, request, render_template, redirect, url_for, flash, session
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with a secure secret key

# MySQL Credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "harigovind",
}

DEPARTMENTS = [
    "Academic Department", "Administrative Department", "Hostel Department",
    "Library Department", "Cafeteria Department", "Placement Department",
    "Technical Support Department", "Transportation Department", "Electrical Maintenance Department"
]

def initialize_department_db(department):
    if not department or not isinstance(department, str) or not department.strip():
        raise ValueError(f"Invalid department name: '{department}'")
    
    db_name = department.lower().replace(" ", "_")
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        conn.commit()
        cursor.close()
        conn.close()

        conn = mysql.connector.connect(database=db_name, **DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grievances (
                tracking_number INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                `class` VARCHAR(50) NOT NULL,
                user_department VARCHAR(100) NOT NULL,
                location TEXT NOT NULL,
                email VARCHAR(255) NOT NULL,
                additional_comments TEXT,
                summary TEXT NOT NULL,
                timestamp DATETIME NOT NULL
            )
        """)
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error initializing '{db_name}': {e}")
        raise
    finally:
        cursor.close()
        conn.close()

def initialize_admin_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS grievance_system")
    conn.commit()
    cursor.close()
    conn.close()

    conn = mysql.connector.connect(database="grievance_system", **DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            department VARCHAR(100) NOT NULL
        )
    """)
    sample_admins = [
        #this is the  user name of admin and their passwords
        ("admin_academic", "password123", "Academic Department"),
        ("admin_hostel", "password123", "Hostel Department"),
        ("admin_library", "password123", "Library Department"),
        ("admin_administrative", "password123", "Administrative Department"),
        ("admin_cafeteria", "password123", "Cafeteria Department"),
        ("admin_placement", "password123", "Placement Department"),
        ("admin_technicalsupport", "password123", "Technical Support Department"),
        ("admin_transport", "password123", "Transportation Department"),
        ("admin_electrical", "password123", "Electrical Maintenance Department"),

    
    ]
    cursor.executemany("INSERT IGNORE INTO admins (username, password, department) VALUES (%s, %s, %s)", sample_admins)
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = mysql.connector.connect(database="grievance_system", **DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM admins WHERE username = %s AND password = %s", (username, password))
        admin = cursor.fetchone()
        cursor.close()
        conn.close()

        if admin:
            session['admin_id'] = admin['id']
            session['department'] = admin['department']
            initialize_department_db(admin['department'])
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials. Please try again.")
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('login'))

    department = session['department']
    db_name = department.lower().replace(" ", "_")

    initialize_department_db(department)

    try:
        conn = mysql.connector.connect(database=db_name, **DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM grievances")
        grievances = cursor.fetchall()
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        flash(f"Error fetching grievances: {e}")
        grievances = []

    if request.method == 'POST':
        tracking_number = request.form['tracking_number']
        move_grievance_to_solved(department, tracking_number)
        flash(f"Grievance {tracking_number} marked as solved.")
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html', grievances=grievances, department=department)

@app.route('/solved_grievances')
def solved_grievances():
    if 'admin_id' not in session:
        return redirect(url_for('login'))

    try:
        conn = mysql.connector.connect(database="solved_grievances", **DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM grievances")
        solved_grievances = cursor.fetchall()
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        flash(f"Error fetching solved grievances: {e}")
        solved_grievances = []

    return render_template('solved_grievances.html', solved_grievances=solved_grievances)

def move_grievance_to_solved(department, tracking_number):
    department_db = department.lower().replace(" ", "_")
    
    try:
        conn = mysql.connector.connect(database=department_db, **DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM grievances WHERE tracking_number = %s", (tracking_number,))
        grievance = cursor.fetchone()
        
        if grievance:
            conn_solved = mysql.connector.connect(database="solved_grievances", **DB_CONFIG)
            cursor_solved = conn_solved.cursor()
            cursor_solved.execute("""
                INSERT INTO grievances (tracking_number, name, `class`, user_department, location, email, additional_comments, summary, resolved_timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (grievance["tracking_number"], grievance["name"], grievance["class"], grievance["user_department"], 
                  grievance["location"], grievance["email"], grievance["additional_comments"], grievance["summary"], datetime.now()))
            conn_solved.commit()
            cursor_solved.close()
            conn_solved.close()
            
            cursor.execute("DELETE FROM grievances WHERE tracking_number = %s", (tracking_number,))
            conn.commit()
    except mysql.connector.Error as e:
        flash(f"Error moving grievance: {e}")
    finally:
        cursor.close()
        conn.close()

@app.route('/logout')
def logout():
    session.pop('admin_id', None)
    session.pop('department', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    initialize_admin_db()
    #app.run(debug=True)
    app.run(debug=True, port=8000)
import mysql.connector
from datetime import datetime

# MySQL Credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "harigovind",
    "database": "solved_grievances"
}

def initialize_solved_grievances_db():
    """Ensures the solved grievances database and table exist."""
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS solved_grievances")
        conn.commit()
        cursor.close()
        conn.close()

        conn = mysql.connector.connect(**DB_CONFIG)
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
                resolved_timestamp DATETIME NOT NULL
            )
        """)
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Database initialization error: {e}")
    finally:
        cursor.close()
        conn.close()


def move_grievance_to_solved(department, tracking_number):
    """Moves a resolved grievance from a department database to the solved grievances table."""
    department_db = department.lower().replace(" ", "_")
    
    try:
        # Connect to the department database
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=department_db
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM grievances WHERE tracking_number = %s", (tracking_number,))
        grievance = cursor.fetchone()
        if not grievance:
            print("No grievance found with this tracking number.")
            return
        
        # Insert into solved grievances table
        conn_solved = mysql.connector.connect(**DB_CONFIG)
        cursor_solved = conn_solved.cursor()
        cursor_solved.execute("""
            INSERT INTO grievances (tracking_number, name, `class`, user_department, location, email, additional_comments, summary, resolved_timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (grievance["tracking_number"], grievance["name"], grievance["class"], grievance["user_department"], 
               grievance["location"], grievance["email"], grievance["additional_comments"], grievance["summary"], datetime.now()))
        conn_solved.commit()
        cursor_solved.close()
        conn_solved.close()
        
        # Delete from original department database
        cursor.execute("DELETE FROM grievances WHERE tracking_number = %s", (tracking_number,))
        conn.commit()
        print("Grievance successfully moved to solved grievances database.")
    except mysql.connector.Error as e:
        print(f"Error moving grievance: {e}")
    finally:
        cursor.close()
        conn.close()

def check_grievance_status(tracking_number):
    """Checks if a grievance is resolved or still pending."""
    try:
        conn_solved = mysql.connector.connect(**DB_CONFIG)
        cursor_solved = conn_solved.cursor()
        cursor_solved.execute("SELECT * FROM grievances WHERE tracking_number = %s", (tracking_number,))
        resolved = cursor_solved.fetchone()
        cursor_solved.close()
        conn_solved.close()
        if resolved:
            print("Your grievance has been resolved.")
        else:
            print("Your grievance is still pending.")
    except mysql.connector.Error as e:
        print(f"Error checking grievance status: {e}")

def insert_test_data():
    """Inserts test grievances into the solved_grievances table."""
    test_data = [
    (100001, "Rahul Sharma", "2nd year", "CSE", "Library", "rahul@karpagamtech.ac.in", "None", "Issue with book return", datetime(2025, 2, 22, 10, 15)),
    (100002, "Meera Ramesh", "3rd year", "IT", "Hostel", "meera@karpagamtech.ac.in", "Complaint about food quality", "Mess food quality is poor", datetime(2025, 2, 21, 16, 00)),
    (100003, "Amit Verma", "1st year", "ECE", "Classroom", "amit@karpagamtech.ac.in", "Fan not working", "Classroom fan is not working properly", datetime(2025, 2, 23, 12, 30))
    ]


    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.executemany("""
        INSERT INTO grievances (tracking_number, name, class, user_department, location, email, additional_comments, summary, resolved_timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", test_data)


        conn.commit()
        print("Test data inserted successfully!")

    except mysql.connector.Error as e:
        print(f"Error inserting test data: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    initialize_solved_grievances_db()
    #insert_test_data()
    # Example usage
    # move_grievance_to_solved("Academic Department", 123456)
    # check_grievance_status(123456)

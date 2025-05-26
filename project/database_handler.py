'''import mysql.connector
from datetime import datetime

# MySQL Credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "harigovind",
}

def initialize_department_db(department):
    """Ensures the department database and grievances table exist with the correct schema."""
    if not department or not isinstance(department, str) or not department.strip():
        raise ValueError(f"Invalid department name: '{department}'")
    
    db_name = department.lower().replace(" ", "_")
    print(f"Initializing database: {db_name}")

    # Connect to MySQL
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise

    # Create database
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        conn.commit()
        print(f"Database '{db_name}' created or already exists")
    except mysql.connector.Error as e:
        print(f"Error creating database '{db_name}': {e}")
        raise
    finally:
        cursor.close()
        conn.close()

    # Connect to the department database
    try:
        conn = mysql.connector.connect(**DB_CONFIG, database=db_name)
        cursor = conn.cursor()
    except mysql.connector.Error as e:
        print(f"Error connecting to database '{db_name}': {e}")
        raise

    # Create or update grievances table
    try:
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
        # Check for tracking_number column
        cursor.execute("SHOW COLUMNS FROM grievances LIKE 'tracking_number'")
        if not cursor.fetchone():
            print(f"Adding missing 'tracking_number' column to '{db_name}'.grievances")
            cursor.execute("ALTER TABLE grievances ADD COLUMN tracking_number INT PRIMARY KEY")
        conn.commit()
        print(f"Table 'grievances' in '{db_name}' created or updated")
    except mysql.connector.Error as e:
        print(f"Error creating/updating table in '{db_name}': {e}")
        raise
    finally:
        cursor.close()
        conn.close()

def store_grievance(department, tracking_number, name, user_class, user_department, location, email, additional_comments, summary):
    """Stores grievance details in the respective department's database."""
    initialize_department_db(department)

    db_name = department.lower().replace(" ", "_")
    print(f"Storing grievance in database: {db_name}")
    
    try:
        conn = mysql.connector.connect(**DB_CONFIG, database=db_name)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO grievances (tracking_number, name, `class`, user_department, location, email, additional_comments, summary, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (tracking_number, name, user_class, user_department, location, email, additional_comments, summary, datetime.now()))
        conn.commit()
        print(f"Grievance successfully inserted into '{db_name}'.grievances")
    except mysql.connector.Error as e:
        print(f"Error inserting data into '{db_name}'.grievances: {e}")
        raise
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    try:
        store_grievance("Academic Department", 123456, "John Doe", "1st year", "CSE", "Library", "john@karpagamtech.ac.in", "None", "Test grievance summary")
    except Exception as e:
        print(f"Test failed: {e}")
'''
import mysql.connector
from datetime import datetime

# MySQL Credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "harigovind",
}

def initialize_department_db(department):
    """Ensures the department database and grievances table exist before inserting data."""
    if not department or not isinstance(department, str) or not department.strip():
        raise ValueError(f"Invalid department name: '{department}'")
    
    db_name = department.lower().replace(" ", "_")  # Convert to lowercase with underscores
    print(f"Initializing database: {db_name}")  # Debug

    # Connect to MySQL (without specifying a database)
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        cursor = conn.cursor()
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")  # Debug
        raise

    # Create department database if not exists
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        conn.commit()
        print(f"Database '{db_name}' created or already exists")  # Debug
    except mysql.connector.Error as e:
        print(f"Error creating database '{db_name}': {e}")  # Debug
        raise
    finally:
        cursor.close()
        conn.close()

    # Now connect to the department database
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=db_name
        )
        cursor = conn.cursor()
    except mysql.connector.Error as e:
        print(f"Error connecting to database '{db_name}': {e}")  # Debug
        raise

    # Create grievances table if not exists
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grievances (
                tracking_number INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                `class` VARCHAR(50) NOT NULL,  -- `class` is a reserved keyword, so use backticks
                user_department VARCHAR(100) NOT NULL,
                location TEXT NOT NULL,
                email VARCHAR(255) NOT NULL,
                additional_comments TEXT,
                summary TEXT NOT NULL,
                timestamp DATETIME NOT NULL
            )
        """)
        conn.commit()
        print(f"Table 'grievances' in '{db_name}' created or already exists")  # Debug
    except mysql.connector.Error as e:
        print(f"Error creating table in '{db_name}': {e}")  # Debug
        raise
    finally:
        cursor.close()
        conn.close()

def store_grievance(department, tracking_number, name, user_class, user_department, location, email, additional_comments, summary):
    """Stores grievance details in the respective department's database."""
    initialize_department_db(department)  # Ensure the database and table exist

    db_name = department.lower().replace(" ", "_")
    print(f"Storing grievance in database: {db_name}")  # Debug
    
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=db_name
        )
        cursor = conn.cursor()
    except mysql.connector.Error as e:
        print(f"Error connecting to database '{db_name}' for insertion: {e}")  # Debug
        raise

    try:
        cursor.execute("""
            INSERT INTO grievances (tracking_number, name, `class`, user_department, location, email, additional_comments, summary, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (tracking_number, name, user_class, user_department, location, email, additional_comments, summary, datetime.now()))
        conn.commit()
        print(f"Grievance successfully inserted into '{db_name}'.grievances")  # Debug
    except mysql.connector.Error as e:
        print(f"Error inserting data into '{db_name}'.grievances: {e}")  # Debug
        raise
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # Test the function
    try:
        store_grievance("Academic Department", 123456, "John Doe", "1st year", "CSE", "Library", "john@karpagamtech.ac.in", "None", "Test grievance summary")
    except Exception as e:
        print(f"Test failed: {e}")

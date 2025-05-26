'''import random
import mysql.connector

# Connect to the MySQL database
def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",  # E.g., "localhost"
        user="root",  # Your MySQL username
        password="harigovind",  # Your MySQL password
        database="tracking_number"  # Your MySQL database name
    )

# Function to generate a unique tracking number
def generate_unique_tracking_number():
    while True:
        # Generate a random 6-digit tracking number
        tracking_number = random.randint(100000, 999999)

        # Connect to the MySQL database and check if the number already exists
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Check if the tracking number already exists
        cursor.execute("SELECT tracking_number FROM tracking_numbers WHERE tracking_number = %s", (str(tracking_number),))
        result = cursor.fetchone()

        if result is None:  # If the number doesn't exist, it's unique
            # Insert the unique tracking number into the database
            cursor.execute("INSERT INTO tracking_numbers (tracking_number) VALUES (%s)", (str(tracking_number),))
            conn.commit()  # Commit the changes
            conn.close()
            return tracking_number  # Return the unique tracking number

        conn.close()  # Close connection if tracking number is not unique

#program for writing in main
'''
import mysql.connector
import random

# Connect to MySQL (without specifying a database initially)
def get_mysql_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="harigovind"
    )
    cursor = conn.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS tracking_number")
    cursor.close()
    conn.close()

    # Now, connect to the tracking_number database
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="harigovind",
        database="tracking_number"
    )

# Function to generate a unique tracking number
def generate_unique_tracking_number():
    conn = get_mysql_connection()
    cursor = conn.cursor()

    # Ensure the tracking_numbers table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracking_numbers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tracking_number VARCHAR(6) UNIQUE NOT NULL
        )
    """)
    conn.commit()

    while True:
        # Generate a random 6-digit tracking number
        tracking_number = str(random.randint(100000, 999999))

        # Check if the tracking number already exists
        cursor.execute("SELECT tracking_number FROM tracking_numbers WHERE tracking_number = %s", (tracking_number,))
        result = cursor.fetchone()

        if result is None:
            # Insert the unique tracking number into the database
            cursor.execute("INSERT INTO tracking_numbers (tracking_number) VALUES (%s)", (tracking_number,))
            conn.commit()
            conn.close()
            return tracking_number  # Return the unique tracking number

        conn.close()  # Close connection if tracking number is not unique

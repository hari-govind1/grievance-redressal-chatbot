import mysql.connector

# MySQL Credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "harigovind",
}

def get_departments_with_data():
    """Fetches all department databases that contain data in the grievances table."""
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cursor = conn.cursor()

    # Get all databases (departments)
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]
    valid_departments = []

    for db in databases:
        try:
            # Connect to department database
            dep_conn = mysql.connector.connect(
                host=DB_CONFIG["host"],
                user=DB_CONFIG["user"],
                password=DB_CONFIG["password"],
                database=db
            )
            dep_cursor = dep_conn.cursor()

            # Check if 'grievances' table exists
            dep_cursor.execute("SHOW TABLES LIKE 'grievances'")
            if dep_cursor.fetchone():
                # Check if grievances table has data
                dep_cursor.execute("SELECT COUNT(*) FROM grievances")
                count = dep_cursor.fetchone()[0]
                if count > 0:
                    valid_departments.append(db)
            
            dep_cursor.close()
            dep_conn.close()
        except mysql.connector.Error:
            continue  # Skip any inaccessible databases

    cursor.close()
    conn.close()
    return valid_departments

def show_data():
    """Displays all grievances from departments that contain data."""
    departments = get_departments_with_data()

    if not departments:
        print("No grievances found in any department.")
        return

    for department in departments:
        print(f"\n📌 Department: {department.replace('_', ' ').title()}")  # Formatting name

        # Connect to department database
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=department
        )
        cursor = conn.cursor()

        # Fetch grievances
        cursor.execute("SELECT * FROM grievances")
        grievances = cursor.fetchall()

        for grievance in grievances:
            print(f"ID: {grievance[0]}")
            print(f"Name: {grievance[1]}")
            print(f"Class: {grievance[2]}")
            print(f"Department: {grievance[3]}")
            print(f"Location: {grievance[4]}")
            print(f"Email: {grievance[5]}")
            print(f"Additional Comments: {grievance[6]}")
            print(f"Summary: {grievance[7]}")
            print(f"Timestamp: {grievance[8]}")
            print("-" * 40)

        cursor.close()
        conn.close()

# Run the function
show_data()

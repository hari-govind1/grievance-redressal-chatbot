import mysql.connector

# MySQL Credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "harigovind",
}

def get_department_databases():
    """Fetches all department databases (excluding system databases)."""
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cursor = conn.cursor()

    # Get all databases
    cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in cursor.fetchall()]

    # Exclude system databases
    system_databases = {"mysql", "performance_schema", "information_schema", "sys"}
    department_databases = [db for db in databases if db not in system_databases]

    cursor.close()
    conn.close()
    return department_databases

def delete_all_departments():
    """Deletes all department databases after user confirmation."""
    departments = get_department_databases()

    if not departments:
        print("No department databases found.")
        return

    print("⚠️ The following department databases will be deleted:")
    for db in departments:
        print(f" - {db.replace('_', ' ').title()}")  # Formatting database names

    confirm = input("Are you sure you want to delete ALL department databases? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Operation canceled.")
        return

    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cursor = conn.cursor()

    # Deleting each database
    for db in departments:
        try:
            cursor.execute(f"DROP DATABASE {db}")
            print(f"✅ Deleted: {db}")
        except mysql.connector.Error as err:
            print(f"❌ Error deleting {db}: {err}")

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ All department databases deleted successfully!")

# Run the function
delete_all_departments()

from db_connect import create_connection

conn = create_connection()

if conn:
    conn.close()
else:
    print("Failed to connect to the database.")

from db_connect import create_connection

conn = create_connection()
cur = conn.cursor()

try:
    cur.execute(
        """
        INSERT INTO users (name, email)
        VALUES (%s, %s)
        """,
        ("Alice", "alice@example.com")
    )
    conn.commit()
    print("User inserted successfully!")
except Exception as e:
    print(f"Failed to insert user: {e}")

cur.close()
conn.close()

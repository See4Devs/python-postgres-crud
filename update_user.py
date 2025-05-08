from db_connect import create_connection

conn = create_connection()
cur = conn.cursor()

try:
    cur.execute(
        """
        UPDATE users
        SET email = %s
        WHERE id = %s
        """,
        ("newalice@example.com", 1)
    )
    conn.commit()
    print("User updated successfully!")
except Exception as e:
    print(f"Failed to update user: {e}")

cur.close()
conn.close()

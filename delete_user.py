from db_connect import create_connection

conn = create_connection()
cur = conn.cursor()

try:
    cur.execute(
        """
        DELETE FROM users
        WHERE id = %s
        """,
        (1,)
    )
    conn.commit()
    print("User deleted successfully!")
except Exception as e:
    print(f"Failed to delete user: {e}")

cur.close()
conn.close()

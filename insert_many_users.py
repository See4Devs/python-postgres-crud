from db_connect import create_connection

# Number of users to insert
x = 20

# Generate dummy users
users = [
    (f"User{i}", f"user{i}@example.com")
    for i in range(1, x + 1)
]

# Connect to the database
conn = create_connection()
cur = conn.cursor()

try:
    # Bulk insert using executemany
    cur.executemany(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        users
    )
    conn.commit()
    print(f"✅ Inserted {cur.rowcount} users successfully!")
except Exception as e:
    conn.rollback()
    print(f"❌ Failed to insert users: {e}")
finally:
    cur.close()
    conn.close()

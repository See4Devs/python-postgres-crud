import psycopg2

def create_connection():
    try:
        conn = psycopg2.connect(
            host="YOUR_HOST",
            database="postgres",
            user="YOUR_USER",
            password="YOUR_PASSWORD",
            port=5432
        )
        print("Connection to the database successful!")
        return conn
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        return None

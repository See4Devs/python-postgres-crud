# PostgreSQL CRUD Operations in Python

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations with PostgreSQL using Python and the `psycopg2` library.

## Author
Lucien Chemaly

## Prerequisites

- Python 3.x
- PostgreSQL database
- psycopg2 library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/See4Devs/python-postgres-crud.git
cd python-postgres-crud
```

2. Create and activate a virtual environment:

For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required package:
```bash
pip install psycopg2-binary
```

4. Verify the installation:
```bash
pip list
```

## Database Configuration

Before running the scripts, update the database connection parameters in `db_connect.py`:

```python
conn = psycopg2.connect(
    host="YOUR_HOST",
    database="postgres",
    user="YOUR_USER",
    password="YOUR_PASSWORD",
    port=5432
)
```

## Project Structure

- `db_connect.py` - Database connection utility
- `test_connection.py` - Test database connectivity
- `insert_user.py` - Insert a single user
- `insert_many_users.py` - Bulk insert multiple users
- `update_user.py` - Update user information
- `delete_user.py` - Delete a user

## Usage Examples

### Test Database Connection
```bash
python test_connection.py
```

### Insert Operations

1. Insert a single user:
```bash
python insert_user.py
```

2. Insert multiple users (20 users by default):
```bash
python insert_many_users.py
```

### Update Operation
```bash
python update_user.py
```

### Delete Operation
```bash
python delete_user.py
```

## Database Schema

The project assumes a `users` table with the following structure:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

## Error Handling

All operations include basic error handling and will:
- Print success messages on successful operations
- Print error messages if operations fail
- Properly close database connections

## Best Practices

1. Always use parameterized queries to prevent SQL injection
2. Properly close database connections after use
3. Use transactions for data consistency
4. Implement error handling for database operations

## Contributing

Feel free to submit issues and enhancement requests!
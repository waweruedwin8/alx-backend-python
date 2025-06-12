import sqlite3
import functools

#### decorator to log SQL queries

def log_queries(func):
    def wrapper(*args, **kwargs):
        # Log the query if it exists in kwargs
        if 'query' in kwargs:
            print(f"Executing query: {kwargs['query']}")
        # Execute the original function
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
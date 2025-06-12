
#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
import os

def stream_users():
    """
    Generator function to stream users from the ALX_prodev database.
    Yields user data as dictionaries.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),  # Gets from environment variable
            database='ALX_prodev',
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
        )
        
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users")
            
            for row in cursor:
                yield row
                
            cursor.close()
            
    except Error as e:
        print(f"Error streaming users: {e}")
        
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
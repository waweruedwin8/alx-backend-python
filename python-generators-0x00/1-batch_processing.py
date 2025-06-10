#!/user/bin/python3
import mysql.connector
from mysql.connector import Error
import os

def stream_users_in_batches(batch_size):
    '''
    Generator function to stream users from the ALX_prodev database in batches.
    Yields a list of user data dictionaries for each batch.
    '''
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
            
            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                    break
                yield batch
            
            cursor.close()
    except Error as e:
        print(f"Error streaming users in batches: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
def batch_processing(batch_size):
    """
    Processes batches of users and filters those over age 25
    
    Args:
        batch_size (int): Size of each batch to process
    """
    # Loop 2: Process each batch from the generator
    for batch in stream_users_in_batches(batch_size):
        # Loop 3: Filter and print users over age 25 from current batch
        for user in batch:
            if user['age'] > 25:
                print(user)
    

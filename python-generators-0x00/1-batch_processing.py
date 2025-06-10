#!/usr/bin/python3
"""
Batch processing module using generators to fetch and process user data.
"""
import mysql.connector
from mysql.connector import Error
import os


def connect_to_prodev():
    """
    Connect to the ALX_prodev database.
    
    Returns:
        mysql.connector.connection: Database connection object
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
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None


def stream_users_in_batches(batch_size):
    """
    Generator that fetches rows in batches from the user_data table.
    
    Args:
        batch_size (int): Number of rows to fetch per batch
        
    Yields:
        list: Batch of user records as dictionaries
    """
    connection = connect_to_prodev()
    if not connection:
        return
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
            
    except Error as e:
        print(f"Error fetching data: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def batch_processing(batch_size):
    """
    Process each batch to filter users over the age of 25.
    
    Args:
        batch_size (int): Size of each batch to process
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
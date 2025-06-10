#!/usr/bin/python3
"""
Database setup script for ALX_prodev MySQL database
Creates database, table, and populates with CSV data
"""

import mysql.connector
import csv
import uuid
import os
from mysql.connector import Error


def connect_db():
    """
    Connects to the MySQL database server
    Returns connection object or None if connection fails
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),  # Gets from environment variable
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
        )
        
        if connection.is_connected():
            print("Successfully connected to MySQL server")
            return connection
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def connect_to_prodev():
    """
    Connects to the ALX_prodev database in MySQL
    Returns connection object or None if connection fails
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
            print("Successfully connected to ALX_prodev database")
            return connection
            
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None


# Rest of your functions remain the same...
def create_database(connection):
    """
    Creates the database ALX_prodev if it does not exist
    Args:
        connection: MySQL connection object
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created successfully or already exists")
        cursor.close()
        
    except Error as e:
        print(f"Error creating database: {e}")


def create_table(connection):
    """
    Creates a table user_data if it does not exist with the required fields
    Args:
        connection: MySQL connection object
    """
    try:
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3,0) NOT NULL,
            INDEX idx_user_id (user_id)
        )
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
        
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_file):
    """
    Inserts data from CSV file into the database if it does not exist
    Args:
        connection: MySQL connection object
        csv_file: Path to the CSV file containing user data
    """
    try:
        cursor = connection.cursor()
        
        # Check if data already exists
        cursor.execute("SELECT COUNT(*) FROM user_data")
        count = cursor.fetchone()[0]
        
        if count > 0:
            print(f"Data already exists in user_data table ({count} rows)")
            cursor.close()
            return
        
        # Read and insert data from CSV
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            insert_query = """
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            """
            
            rows_inserted = 0
            for row in csv_reader:
                # Generate UUID for user_id if not present in CSV
                user_id = row.get('user_id', str(uuid.uuid4()))
                name = row.get('name', '')
                email = row.get('email', '')
                age = int(float(row.get('age', 0)))
                
                cursor.execute(insert_query, (user_id, name, email, age))
                rows_inserted += 1
            
            connection.commit()
            print(f"Successfully inserted {rows_inserted} rows into user_data table")
        
        cursor.close()
        
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found")
    except Error as e:
        print(f"Error inserting data: {e}")
        connection.rollback()
    except Exception as e:
        print(f"Unexpected error: {e}")
        connection.rollback()


if __name__ == "__main__":
    # Test the functions
    conn = connect_db()
    if conn:
        create_database(conn)
        conn.close()
        
        prodev_conn = connect_to_prodev()
        if prodev_conn:
            create_table(prodev_conn)
            insert_data(prodev_conn, 'user_data.csv')
            prodev_conn.close()
#!/usr/bin/python3
"""
Memory-efficient aggregate function using generators to compute average age.
"""

import seed


def stream_user_ages():
    """
    Generator that yields user ages one by one from the database.
    
    Yields:
        int: User age
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row['age']
    
    connection.close()


def calculate_average_age():
    """
    Calculate the average age of users using the generator.
    Does not load the entire dataset into memory.
    
    Returns:
        float: Average age of users
    """
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    return total_age / count if count > 0 else 0


if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age}")
#!/usr/bin/python3
"""
Lazy pagination module using generators to fetch paginated data.
"""

import seed


def paginate_users(page_size, offset):
    """
    Fetch a page of users from the database.
    
    Args:
        page_size (int): Number of users per page
        offset (int): Starting position for the page
        
    Returns:
        list: List of user records as dictionaries
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator that lazily loads paginated data from the users database.
    Only fetches the next page when needed.
    
    Args:
        page_size (int): Number of users per page
        
    Yields:
        list: Page of user records as dictionaries
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
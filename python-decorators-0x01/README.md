# Python Decorators - 0x01

## Project Overview

This project focuses on mastering Python decorators to enhance database operations in Python applications. Through hands-on tasks, learners will create custom decorators to log queries, handle connections, manage transactions, retry failed operations, and cache query results.

## 📋 Project Information

- **Level**: Novice
- **Weight**: 1
- **Duration**: May 19, 2025 12:00 AM to May 26, 2025 12:00 AM
- **Repository**: `alx-backend-python`
- **Directory**: `python-decorators-0x01`

## 🎯 Learning Objectives

By completing these tasks, professional developers will:

- Deepen their knowledge of Python decorators and how they can be used to create reusable, efficient, and clean code
- Enhance database management skills by automating repetitive tasks like connection handling, logging, and caching
- Implement robust transaction management techniques to ensure data integrity and handle errors gracefully
- Optimize database queries by leveraging caching mechanisms to reduce redundant calls
- Build resilience into database operations by implementing retry mechanisms for transient errors
- Apply best practices in database interaction for scalable and maintainable Python applications

## 📋 Requirements

- Python 3.8 or higher installed
- SQLite3 database setup with a users table for testing
- A working knowledge of Python decorators and database operations
- Familiarity with Git and GitHub for project submission
- Strong problem-solving skills and attention to detail

## 📝 Tasks Overview

### Task 0: Logging Database Queries
**File**: `0-log_queries.py`

Create a decorator that logs all SQL queries executed by a function. Learn to intercept function calls to enhance observability.

**Prototype**: `def log_queries()`

**Example Usage**:
```python
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

users = fetch_all_users(query="SELECT * FROM users")
```

### Task 1: Handle Database Connections with a Decorator
**File**: `1-with_db_connection.py`

Automate database connection handling with a decorator. Eliminate boilerplate code for opening and closing connections.

**Prototype**: `def with_db_connection(func)`

**Example Usage**:
```python
@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone()

user = get_user_by_id(user_id=1)
```

### Task 2: Transaction Management Decorator
**File**: `2-transactional.py`

Implement a decorator to manage database transactions (commit/rollback). Ensure robust error handling and data consistency.

**Prototype**: `def transactional(func)`

**Example Usage**:
```python
@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

update_user_email(user_id=1, new_email='new@email.com')
```

### Task 3: Retry Database Queries
**File**: `3-retry_on_failure.py`

Build a decorator to retry database operations on failure. Introduce resilience against transient database issues.

**Prototype**: `def retry_on_failure(retries=3, delay=2)`

**Example Usage**:
```python
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

users = fetch_users_with_retry()
```

### Task 4: Cache Database Queries
**File**: `4-cache_query.py`

Implement a decorator to cache query results. Optimize performance by avoiding redundant database calls.

**Prototype**: `def cache_query(func)`

**Example Usage**:
```python
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
```

## 🛠️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/alx-backend-python.git
   cd alx-backend-python/python-decorators-0x01
   ```

2. **Set up SQLite database** (if needed):
   ```python
   import sqlite3
   
   conn = sqlite3.connect('users.db')
   cursor = conn.cursor()
   cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           email TEXT NOT NULL
       )
   ''')
   conn.commit()
   conn.close()
   ```

3. **Run the tasks**:
   ```bash
   python3 0-log_queries.py
   python3 1-with_db_connection.py
   python3 2-transactional.py
   python3 3-retry_on_failure.py
   python3 4-cache_query.py
   ```

## 🔍 Key Concepts

### Python Decorators
- Function wrappers that modify or enhance function behavior
- Use `@decorator_name` syntax above function definitions
- Can accept parameters and return modified functions

### Database Management Patterns
- **Connection Handling**: Automatic opening/closing of database connections
- **Transaction Management**: Ensuring ACID properties with commit/rollback
- **Error Handling**: Graceful handling of database errors
- **Performance Optimization**: Caching and retry mechanisms

### Best Practices
- Use `functools.wraps` to preserve original function metadata
- Handle exceptions appropriately in decorators
- Implement proper resource cleanup (connections, cursors)
- Consider thread safety for production applications

## 📊 Progress Tracking

- [ ] Task 0: Logging Database Queries
- [ ] Task 1: Handle Database Connections
- [ ] Task 2: Transaction Management
- [ ] Task 3: Retry Database Queries
- [ ] Task 4: Cache Database Queries

## 🚀 Advanced Features

### Decorator Stacking
Multiple decorators can be applied to a single function:
```python
@with_db_connection
@transactional
@retry_on_failure(retries=3)
@cache_query
def complex_database_operation(conn, query):
    # Function implementation
    pass
```

### Error Handling
Implement comprehensive error handling for different database scenarios:
- Connection failures
- Query syntax errors
- Transaction conflicts
- Timeout issues

## 📚 Resources

- [Python Decorators Documentation](https://docs.python.org/3/glossary.html#term-decorator)
- [SQLite3 Python Tutorial](https://docs.python.org/3/library/sqlite3.html)
- [Database Design Best Practices](https://www.sqlstyle.guide/)
- [Python functools Module](https://docs.python.org/3/library/functools.html)

## 📝 Notes

- Ensure all files are properly named and placed in the correct directory
- Test each decorator individually before combining them
- Pay attention to the order of decorator application
- Consider edge cases and error scenarios in your implementations

---

**Author**: ALX Backend Python Program  
**Version**: 1.0  
**Last Updated**: June 2025
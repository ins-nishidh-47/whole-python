# mysql_connector.py: Learn how to use MySQL Connector in Python

import mysql.connector
from mysql.connector import Error

# Function to establish a connection to the MySQL database
def create_connection(host, user, password, database=None):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print(f"Connected to the database: {host}")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to close the connection to the database
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection closed.")

# Function to execute a single query (e.g., SELECT, INSERT, UPDATE, DELETE)
def execute_query(connection, query, data=None):
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()  # Commit the changes
        print(f"Query executed successfully: {query}")
    except Error as e:
        print(f"Error: {e}")

# Function to execute a SELECT query and fetch all results
def fetch_all_results(connection, query, data=None):
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to fetch one result from a SELECT query
def fetch_one_result(connection, query, data=None):
    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        result = cursor.fetchone()
        return result
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to create a new table
def create_table(connection, table_name, columns):
    try:
        cursor = connection.cursor()
        query = f"CREATE TABLE {table_name} ({columns})"
        cursor.execute(query)
        print(f"Table {table_name} created successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to insert data into a table
def insert_data(connection, table, columns, values):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO {table} ({columns}) VALUES ({', '.join(['%s'] * len(values))})"
        cursor.execute(query, values)
        connection.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to update data in a table
def update_data(connection, table, set_values, where_condition):
    try:
        cursor = connection.cursor()
        query = f"UPDATE {table} SET {set_values} WHERE {where_condition}"
        cursor.execute(query)
        connection.commit()
        print("Data updated successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to delete data from a table
def delete_data(connection, table, where_condition):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM {table} WHERE {where_condition}"
        cursor.execute(query)
        connection.commit()
        print("Data deleted successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to drop a table
def drop_table(connection, table_name):
    try:
        cursor = connection.cursor()
        query = f"DROP TABLE IF EXISTS {table_name}"
        cursor.execute(query)
        print(f"Table {table_name} dropped successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to check if a table exists
def check_table_exists(connection, table_name):
    try:
        cursor = connection.cursor()
        query = f"SHOW TABLES LIKE '{table_name}'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result is not None
    except Error as e:
        print(f"Error: {e}")
        return False

# Function to create a database
def create_database(connection, db_name):
    try:
        cursor = connection.cursor()
        query = f"CREATE DATABASE {db_name}"
        cursor.execute(query)
        print(f"Database {db_name} created successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to list all databases
def list_databases(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        return databases
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to switch between databases
def switch_database(connection, db_name):
    try:
        connection.database = db_name
        print(f"Switched to database: {db_name}")
    except Error as e:
        print(f"Error: {e}")

# Example usage of MySQL connector functions
def mysql_example_usage():
    # Create a connection to the MySQL server
    connection = create_connection("localhost", "root", "your_password", "test_db")

    if connection:
        # Create a table
        create_table(connection, "employees", "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT")
        
        # Insert data into the table
        insert_data(connection, "employees", "name, age", ("John Doe", 30))
        insert_data(connection, "employees", "name, age", ("Jane Smith", 28))
        
        # Update data
        update_data(connection, "employees", "age = 31", "name = 'John Doe'")
        
        # Fetch all data
        results = fetch_all_results(connection, "SELECT * FROM employees")
        for result in results:
            print(result)
        
        # Delete data
        delete_data(connection, "employees", "name = 'Jane Smith'")
        
        # Drop the table
        drop_table(connection, "employees")

        # Close the connection
        close_connection(connection)

if __name__ == "__main__":
    mysql_example_usage()

# exception_handling.py

# Basic Try-Except
def basic_exception_handling(a, b):
    try:
        result = a / b
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Multiple Exceptions
def multiple_exceptions_handling(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range."
    except TypeError:
        return "Error: Invalid input type."

# Using Else Clause
def exception_with_else(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"Division successful: {result}"

# Using Finally Clause
def exception_with_finally(file_path):
    try:
        file = open(file_path, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        return "Error: File not found."
    finally:
        print("Execution completed, closing file if opened.")
        try:
            file.close()
        except:
            pass  # Handle cases where the file couldn't be opened

# Custom Exception
class CustomError(Exception):
    """Custom exception class"""
    pass

def raise_custom_exception(value):
    if value < 0:
        raise CustomError("Value cannot be negative!")
    return f"Valid value: {value}"

# Handling Multiple Exceptions with a Single Except
def multiple_exceptions_in_one(a, b, key):
    try:
        result = a / b
        dictionary = {"key1": "value1"}
        return dictionary[key]
    except (ZeroDivisionError, KeyError) as e:
        return f"Error: {str(e)}"

# Exception Chaining
def exception_chaining_example():
    try:
        try:
            int("not_a_number")
        except ValueError as e:
            raise TypeError("A TypeError occurred") from e
    except Exception as e:
        return f"Chained Exception: {str(e)}"

# Catch-All Exception Handling
def catch_all_exceptions(a, b):
    try:
        return a / b
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# methods.py


def default_functions():
    return {
        "len": len("Hello"),  # Returns the length of the string
        "type": type(123),  # Returns the type of the object
        "id": id("sample"),  # Returns the identity of the object
        "repr": repr("Hello"),  # Returns a string representation of the object
        "callable": callable(print),  # Checks if an object is callable
        "sorted": sorted([5, 2, 9, 1]),  # Sorts a list
        "min": min([1, 5, 2, 9]),  # Returns the smallest item in an iterable
        "max": max([1, 5, 2, 9]),  # Returns the largest item in an iterable
        "sum": sum([1, 2, 3]),  # Returns the sum of all items in an iterable
        "all": all([True, False, True]),  # Checks if all elements are true
        "any": any([True, False, False]),  # Checks if any element is true
        "abs": abs(-7),  # Absolute value of a number
        "enumerate": list(enumerate(["apple", "banana", "cherry"])),  # Adds index to iterable
        "zip": list(zip([1, 2, 3], ["a", "b", "c"])),  # Zips two iterables together
        "filter": list(filter(lambda x: x > 2, [1, 2, 3, 4])),  # Filters elements based on condition
        "map": list(map(lambda x: x * 2, [1, 2, 3])),  # Applies a function to all items
        "range": list(range(1, 6)),  # Generates a sequence of numbers
        "chr": chr(97),  # Converts an ASCII code to a character
        "ord": ord('a'),  # Converts a character to its ASCII code
        "reversed": list(reversed([1, 2, 3])),  # Reverses an iterable
        "isinstance": isinstance(123, int),  # Checks if an object is an instance of a class
        "round": round(3.14159, 2),  # Rounds a number to a given precision
        "divmod": divmod(10, 3),  # Returns a tuple of (quotient, remainder)
        "eval": eval("2 + 3"),  # Evaluates a string as Python code
        "exec": exec('a = 5; print(a)'),  # Executes dynamically created Python code
        "format": "Hello, {}!".format("World"),  # String formatting using .format()
        "hex": hex(255),  # Returns the hexadecimal representation of a number
        "oct": oct(8),  # Returns the octal representation of a number
    }

# String Methods
def string_methods(s):
    return {
        "lower": s.lower(),
        "upper": s.upper(),
        "title": s.title(),
        "capitalize": s.capitalize(),
        "replace": s.replace("hello", "hi"),
        "split": s.split(),
        "strip": s.strip(),
        "find": s.find("e"),
        "count": s.count("l"),
        "startswith": s.startswith("H"),
        "endswith": s.endswith("o"),
        "isalpha": s.isalpha(),
        "isdigit": s.isdigit(),
        "isnumeric": s.isnumeric(),
        "isspace": s.isspace(),
    }

# List Methods
def list_methods(lst):
    return {
        "append": lst.append(4),  # Adds 4 to the list
        "extend": lst.extend([5, 6]),  # Adds multiple elements
        "insert": lst.insert(1, 10),  # Inserts 10 at index 1
        "remove": lst.remove(10),  # Removes the first occurrence of 10
        "pop": lst.pop(),  # Removes the last item
        "clear": lst.clear(),  # Clears the entire list
        "index": lst.index(2),  # Returns the index of first occurrence of 2
        "count": lst.count(1),  # Counts how many times 1 occurs
        "sort": lst.sort(),  # Sorts the list in ascending order
        "reverse": lst.reverse(),  # Reverses the list
        "copy": lst.copy(),  # Creates a shallow copy of the list
        "join": ', '.join(map(str, lst)),  # Joins list elements into a string
    }

# Dictionary Methods
def dictionary_methods(d):
    return {
        "get": d.get("key1", "Not Found"),  # Returns value for 'key1'
        "keys": list(d.keys()),  # Returns all keys
        "values": list(d.values()),  # Returns all values
        "items": list(d.items()),  # Returns a list of key-value pairs
        "update": d.update({"key3": "value3"}),  # Adds a new key-value pair
        "pop": d.pop("key1", "Key not found"),  # Removes key 'key1'
        "popitem": d.popitem(),  # Removes the last key-value pair
        "clear": d.clear(),  # Clears the entire dictionary
        "setdefault": d.setdefault("key4", "default_value"),  # Sets default value
    }

# Set Methods
def set_methods(s):
    return {
        "add": s.add(4),  # Adds 4 to the set
        "remove": s.remove(4),  # Removes 4 from the set
        "discard": s.discard(5),  # Discards 5 from the set without error
        "pop": s.pop(),  # Removes a random element
        "clear": s.clear(),  # Clears the set
        "union": s.union({1, 2, 3}),  # Returns a set with elements from both sets
        "intersection": s.intersection({2, 3, 4}),  # Returns common elements
        "difference": s.difference({1, 2}),  # Returns elements in s but not in {1, 2}
        "issubset": s.issubset({1, 2, 3, 4}),  # Checks if s is a subset
        "issuperset": s.issuperset({2, 3}),  # Checks if s is a superset
        "copy": s.copy(),  # Creates a shallow copy of the set
    }

# Tuple Methods (Immutable, but you can perform some operations like counting and indexing)
def tuple_methods(t):
    return {
        "count": t.count(2),  # Counts occurrences of 2
        "index": t.index(3),  # Returns the index of first occurrence of 3
    }

# Function Methods (such as map, filter, reduce)
def function_methods():
    lst = [1, 2, 3, 4, 5]

    # Using map to apply a function to each item
    doubled = list(map(lambda x: x * 2, lst))

    # Using filter to filter out odd numbers
    even = list(filter(lambda x: x % 2 == 0, lst))

    # Using reduce to accumulate results (requires functools)
    from functools import reduce
    sum_all = reduce(lambda x, y: x + y, lst)

    return {
        "map": doubled,
        "filter": even,
        "reduce": sum_all,
    }

# Math Functions
import math
def math_methods():
    return {
        "abs": abs(-7),  # Absolute value
        "pow": pow(2, 3),  # 2 raised to the power of 3
        "sqrt": math.sqrt(16),  # Square root of 16
        "max": max([1, 5, 2, 9]),  # Maximum value
        "min": min([1, 5, 2, 9]),  # Minimum value
        "round": round(3.14159, 2),  # Rounds to 2 decimal places
        "factorial": math.factorial(5),  # 5!
    }

# File Methods
def file_methods(file_path):
    try:
        with open(file_path, "w") as file:
            file.write("Hello, World!")
        
        with open(file_path, "r") as file:
            content = file.read()

        return {
            "read": content,
            "seek": "File pointer moved back to start",
            "close": "File is automatically closed after the block",
        }
    except Exception as e:
        return f"Error: {e}"



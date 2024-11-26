    # operators.py

# Arithmetic Operators
def arithmetic_operations(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else "Division by zero error",
        "floor_division": a // b if b != 0 else "Division by zero error",
        "modulus": a % b if b != 0 else "Division by zero error",
        "exponentiation": a ** b,
    }

# Comparison Operators
def comparison_operations(a, b):
    return {
        "equal_to": a == b,
        "not_equal_to": a != b,
        "greater_than": a > b,
        "less_than": a < b,
        "greater_than_or_equal_to": a >= b,
        "less_than_or_equal_to": a <= b,
    }

# Logical Operators
def logical_operations(a, b):
    return {
        "and": a and b,
        "or": a or b,
        "not_a": not a,
        "not_b": not b,
    }

# Bitwise Operators
def bitwise_operations(a, b):
    return {
        "and": a & b,
        "or": a | b,
        "xor": a ^ b,
        "not_a": ~a,
        "left_shift": a << b,
        "right_shift": a >> b,
    }

# Assignment Operators
def assignment_operations(a, b):
    results = {}
    results["add_assign"] = a + b
    results["subtract_assign"] = a - b
    results["multiply_assign"] = a * b
    if b != 0:
        results["divide_assign"] = a / b
        results["modulus_assign"] = a % b
    else:
        results["divide_assign"] = "Division by zero error"
        results["modulus_assign"] = "Division by zero error"
    return results

# Identity Operators
def identity_operations(a, b):
    return {
        "is": a is b,
        "is_not": a is not b,
    }

# Membership Operators
def membership_operations(element, iterable):
    return {
        "in": element in iterable,
        "not_in": element not in iterable,
    }

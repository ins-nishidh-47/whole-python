# methods.py (Handling All Built-in Errors)

def all_error_handling():
    result = {}
    
    # Handling different types of built-in exceptions
    
    try:
        # ZeroDivisionError
        a = 10 / 0
    except ZeroDivisionError as e:
        result["ZeroDivisionError"] = f"Caught an error: {str(e)}"
    
    try:
        # IndexError
        lst = [1, 2, 3]
        value = lst[5]
    except IndexError as e:
        result["IndexError"] = f"Caught an error: {str(e)}"
    
    try:
        # KeyError
        d = {"a": 1}
        value = d["b"]
    except KeyError as e:
        result["KeyError"] = f"Caught an error: {str(e)}"
    
    try:
        # TypeError
        x = "10" + 5
    except TypeError as e:
        result["TypeError"] = f"Caught an error: {str(e)}"
    
    try:
        # ValueError
        num = int("Hello")
    except ValueError as e:
        result["ValueError"] = f"Caught an error: {str(e)}"
    
    try:
        # FileNotFoundError
        with open("non_existent_file.txt", "r") as file:
            file.read()
    except FileNotFoundError as e:
        result["FileNotFoundError"] = f"Caught an error: {str(e)}"
    
    try:
        # AttributeError
        NoneType = None
        NoneType.some_method()
    except AttributeError as e:
        result["AttributeError"] = f"Caught an error: {str(e)}"
    
    try:
        # ImportError
        import kiwy
    except ImportError as e:
        result["ImportError"] = f"Caught an error: {str(e)}"
    
    try:
        # SyntaxError
        eval('if True print("Hello")')
    except SyntaxError as e:
        result["SyntaxError"] = f"Caught an error: {str(e)}"
    
    try:
        # OverflowError
        x = 10 ** 1000  # Big number that exceeds the limit
    except OverflowError as e:
        result["OverflowError"] = f"Caught an error: {str(e)}"
    
    try:
        # RecursionError
        def recursive_call():
            return recursive_call()
        recursive_call()
    except RecursionError as e:
        result["RecursionError"] = f"Caught an error: {str(e)}"
    
    try:
        # IndentationError
        eval('  print("Hello")')  # Intentional indentation mistake
    except IndentationError as e:
        result["IndentationError"] = f"Caught an error: {str(e)}"
    
    try:
        # StopIteration
        iter_obj = iter([1, 2])
        next(iter_obj)
        next(iter_obj)
        next(iter_obj)  # This will raise StopIteration
    except StopIteration as e:
        result["StopIteration"] = f"Caught an error: {str(e)}"
    
    try:
        # FileExistsError
        import os
        os.mkdir('existing_dir')
        os.mkdir('existing_dir')  # Will cause FileExistsError
    except FileExistsError as e:
        result["FileExistsError"] = f"Caught an error: {str(e)}"
    
    try:
        # PermissionError
        with open('protected_file.txt', 'w') as file:
            file.write("This file is protected!")  # This will raise PermissionError if file is read-only
    except PermissionError as e:
        result["PermissionError"] = f"Caught an error: {str(e)}"
    
    try:
        # RuntimeError
        raise RuntimeError("This is a runtime error!")
    except RuntimeError as e:
        result["RuntimeError"] = f"Caught an error: {str(e)}"
    
    try:
        # NotImplementedError
        def unimplemented_method():
            raise NotImplementedError("This method is not implemented yet.")
        unimplemented_method()
    except NotImplementedError as e:
        result["NotImplementedError"] = f"Caught an error: {str(e)}"
    
    try:
        # MemoryError
        big_list = [1] * (10 ** 10)  # This might raise a MemoryError depending on the system
    except MemoryError as e:
        result["MemoryError"] = f"Caught an error: {str(e)}"
    
    try:
        # AssertionError
        assert 5 == 10, "Assertion failed"
    except AssertionError as e:
        result["AssertionError"] = f"Caught an error: {str(e)}"
    
    try:
        # UnboundLocalError
        def test_local():
            print(a)
            a = 10
        test_local()
    except UnboundLocalError as e:
        result["UnboundLocalError"] = f"Caught an error: {str(e)}"
    
    try:
        # OSError
        os.remove("non_existent_file.txt")
    except OSError as e:
        result["OSError"] = f"Caught an error: {str(e)}"
    
    try:
        # NotImplementedError (again)
        raise NotImplementedError("Not yet implemented feature!")
    except NotImplementedError as e:
        result["NotImplementedError"] = f"Caught an error: {str(e)}"

    return result



# Handling Custom Exceptions
class CustomError(Exception):
    """A custom exception for specific error handling."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def raise_custom_error():
    try:
        raise CustomError("This is a custom exception!")
    except CustomError as e:
        return f"Caught a custom error: {str(e)}"


# Handling Assertions
def assertion_example():
    try:
        x = 5
        assert x == 10, "x should be equal to 10"
    except AssertionError as e:
        return f"AssertionError: {str(e)}"
    return "No assertion errors!"
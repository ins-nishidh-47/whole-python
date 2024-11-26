# loops.py

# For Loop: Iterating through a list
def for_loop_example(lst):
    result = []
    for item in lst:
        result.append(item * 2)  # Example: Multiply each element by 2
    return result

# For Loop with Range
def for_loop_with_range(start, end, step=1):
    result = []
    for i in range(start, end, step):
        result.append(i)
    return result

# Nested For Loop
def nested_for_loop(matrix):
    result = []
    for row in matrix:
        row_result = []
        for element in row:
            row_result.append(element ** 2)  # Example: Square each element
        result.append(row_result)
    return result

# While Loop
def while_loop_example(limit):
    result = []
    count = 0
    while count < limit:
        result.append(count)
        count += 1  # Increment count
    return result

# While Loop with Break
def while_loop_with_break(limit):
    result = []
    count = 0
    while True:
        if count >= limit:
            break  # Exit the loop when the limit is reached
        result.append(count)
        count += 1
    return result

# While Loop with Continue
def while_loop_with_continue(limit):
    result = []
    count = 0
    while count < limit:
        count += 1
        if count % 2 == 0:  # Skip even numbers
            continue
        result.append(count)
    return result

# Looping with Else (For Loop)
def for_loop_with_else(lst):
    for item in lst:
        if item == 0:
            return "Zero found!"  # Exit early if 0 is found
    else:
        return "No zeros found!"

# Looping with Else (While Loop)
def while_loop_with_else(limit):
    count = 0
    while count < limit:
        if count == 3:
            break  # Break the loop if count is 3
        count += 1
    else:
        return "Loop completed without break"
    return "Loop exited early"

# Infinite Loop (Example)
def infinite_loop_example():
    count = 0
    while True:
        print("This is an infinite loop. Press Ctrl+C to stop.")
        count += 1
        if count == 5:  # Stop after 5 iterations for demonstration
            break
    return "Stopped after 5 iterations"

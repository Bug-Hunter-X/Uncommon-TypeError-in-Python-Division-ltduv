def function_with_uncommon_error_solution(a, b):
    try:
        if isinstance(a, str) or isinstance(b, str):
            print("Error: Cannot divide strings")
            return None
        if b == 0:
            print("Error: Division by zero")
            return None
        result = a / b
        return result
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

result1 = function_with_uncommon_error_solution(10, 2)  # Output: 5.0
result2 = function_with_uncommon_error_solution(10, 0)  # Output: Error: Division by zero, None
result3 = function_with_uncommon_error_solution("hello", 2) # Output: Error: Cannot divide strings, None
result4 = function_with_uncommon_error_solution(10, "world") # Output: Error: Cannot divide strings, None
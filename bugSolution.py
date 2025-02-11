def function_with_improved_error_handling(a, b):
    try:
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            raise TypeError("Inputs must be numbers")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        return result
    except TypeError as e:
        return f"TypeError: {e}"
    except ZeroDivisionError as e:
        return f"ZeroDivisionError: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage:
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: ZeroDivisionError: Cannot divide by zero
print(function_with_improved_error_handling(10, "2")) # Output: TypeError: Inputs must be numbers
print(function_with_improved_error_handling("10", 2)) # Output: TypeError: Inputs must be numbers
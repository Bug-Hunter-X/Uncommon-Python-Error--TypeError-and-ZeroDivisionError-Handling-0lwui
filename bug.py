def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        return "TypeError: unsupported operand type(s) for /: 'str' and 'int'"
    except ZeroDivisionError:
        return "ZeroDivisionError: division by zero"

# Example usage:
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: ZeroDivisionError: division by zero
print(function_with_uncommon_error(10, "2")) # Output: TypeError: unsupported operand type(s) for /: 'int' and 'str'
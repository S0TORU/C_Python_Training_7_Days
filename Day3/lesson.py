# This program demonstrates functions and modular programming in Python.
# Functions are defined with def, support various parameter types.
# Best practice: Use type hints and docstrings for clarity.

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

def factorial(n: int) -> int:
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def print_hello() -> None:
    """Print a greeting."""
    print("Hello from a function!")

# Main execution
if __name__ == "__main__":  # Best practice: Guard for script execution
    # Example 1: Function call
    sum_result = add(5, 3)
    print(f"5 + 3 = {sum_result}")

    # Example 2: Recursive function
    num = 5
    fact = factorial(num)
    print(f"Factorial of {num} is {fact}")

    # Example 3: Modular call
    print_hello()

    # Note: Python functions can return multiple values, use *args/**kwargs for flexibility

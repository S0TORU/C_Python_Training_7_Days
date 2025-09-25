# This program demonstrates basic variables, data types, and I/O in Python.
# It reads user input for name, age, and height, then prints a formatted message.
# Best practice: Use type hints for clarity and error prevention in larger codebases.

# No need for explicit declarations; variables are dynamically typed
name: str = input("Enter your name: ")  # String input
age: int = int(input("Enter your age: "))  # Convert to int
height: float = float(input("Enter your height in meters: "))  # Convert to float

# Output using f-string for modern, readable formatting
print(f"Hello {name}, you are {age} years old and {height:.2f} meters tall.")

# Note: Python handles type conversion explicitly, unlike C's scanf.
# This program is simpler but requires careful input validation for robustness.

# This program demonstrates control structures in Python: conditionals and loops.
# It includes examples of if-elif-else and for/while loops.
# Best practice: Use descriptive names and leverage Python's iterable nature.

# Example 1: Conditional - Check if a number is even or odd
num = 7  # Example number
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Example 2: Loop - Print numbers from 1 to 10 using for loop
print("Numbers from 1 to 10:")
for i in range(1, 11):  # range(start, end) end exclusive
    print(i, end=" ")
print()  # Newline

# Example 3: While loop - Simple countdown
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blast off!")

# Example 4: FizzBuzz logic in a loop (from exercises)
print("FizzBuzz from 1 to 20:")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# Note: Python's for loop is powerful for iterating over lists, strings, etc.
# Example: Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

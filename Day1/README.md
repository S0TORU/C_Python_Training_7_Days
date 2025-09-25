# Day 1: Variables, Data Types, and Basic I/O

## Overview
Today, we dive into the fundamentals of programming: variables, data types, and basic input/output operations. Given your background in building systems and training models, we'll emphasize how these concepts apply to scalable and efficient code. We'll compare C and Python to highlight their differences and strengths.

## Key Concepts
- **Variables**: Named storage locations for data.
- **Data Types**: Define the kind of data a variable can hold (e.g., integers, floats, strings).
- **Basic I/O**: Reading input from the user and displaying output.

## C Language Section

### Variables and Data Types
In C, variables must be explicitly declared with a data type. This static typing helps catch errors at compile-time and optimizes performance.

Common data types:
- `int`: For integers (e.g., 42)
- `float`: For single-precision floating-point numbers (e.g., 3.14)
- `double`: For double-precision floating-point numbers (higher precision than float)
- `char`: For single characters (e.g., 'A')

Variables are declared like: `int age = 25;`

### Basic I/O
- **Output**: Use `printf()` from `<stdio.h>`
- **Input**: Use `scanf()` from `<stdio.h>`

Remember to include headers and handle errors.

### Example Code
See `lesson.c` for a complete example with comments.

## Python Language Section

### Variables and Data Types
Python uses dynamic typing, where variables can hold any type of data, and types are inferred at runtime. This flexibility speeds up development but requires careful testing.

Common data types:
- `int`: Integers
- `float`: Floating-point numbers
- `str`: Strings
- `bool`: Booleans
- `list`: Mutable sequences
- `dict`: Key-value pairs

Variables are assigned like: `age = 25`

### Basic I/O
- **Output**: Use `print()` function
- **Input**: Use `input()` function (returns a string)

Python's I/O is simpler and more forgiving.

### Example Code
See `lesson.py` for a complete example with comments.

## Best Practices
- In C: Always initialize variables to avoid undefined behavior.
- In Python: Use descriptive variable names; leverage built-in type hints for clarity (e.g., `age: int = 25`).
- Write modular code: Even in simple programs, separate logic into functions.
- Add comments: Explain what each part does.
- Test your code: Run and verify outputs.

## Exercises
1. **C and Python**: Write a program that declares variables for name (string), age (int), and height (float). Read these from user input and print them back in a formatted message.
2. **Comparison**: Note how C requires explicit type declarations while Python does not. How might this affect scalability in large projects?
3. **Advanced**: In Python, explore type conversion (e.g., `int(input())`). In C, handle scanf errors.

Compile and run your programs. If you encounter issues, debug by adding print statements or using a debugger.

## Next Steps
Tomorrow, we'll cover control structures like loops and conditionals to add logic to your programs.

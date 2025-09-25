# Day 3: Functions and Modular Programming

## Overview
Today, we learn about functions, the building blocks of modular code. Functions encapsulate logic, promote reusability, and make code easier to test and maintain. We'll define functions, pass parameters, and return values in C and Python, with a focus on writing scalable, manageable code.

## Key Concepts
- **Functions**: Reusable blocks of code that perform specific tasks.
- **Parameters and Return Values**: Passing data in and out.
- **Modularity**: Breaking code into smaller, focused units.
- **Scope**: Where variables are accessible.

## C Language Section

### Defining Functions
Functions are declared with return type, name, parameters.

Syntax:
```c
return_type function_name(parameter_list) {
    // body
    return value;
}
```

Prototypes are often declared at the top.

### Example Code
See `lesson.c` for function examples, including recursion.

## Python Language Section

### Defining Functions
Use `def` keyword. No need for prototypes.

Syntax:
```python
def function_name(parameters):
    # body
    return value
```

Python supports default arguments, *args, **kwargs.

### Example Code
See `lesson.py` for function examples.

## Best Practices
- In C: Declare function prototypes to avoid implicit declarations.
- In Python: Use type hints for parameters and returns.
- Write docstrings: Document what functions do.
- Keep functions small and single-purpose.
- Test functions independently.

## Exercises
1. **C and Python**: Write a function to calculate factorial recursively. Call it from main.
2. **Modularity**: Refactor Day 1's I/O program into functions (e.g., get_user_input, display_info).
3. **Comparison**: Discuss how C's static typing vs. Python's dynamic typing affects function design.

## Next Steps
Day 4 dives into pointers in C and data structures in Python for handling complex data.

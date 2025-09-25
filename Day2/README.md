# Day 2: Control Structures - Conditionals and Loops

## Overview
Building on Day 1, today we explore control structures that allow programs to make decisions and repeat actions. Conditionals (if-else) handle branching logic, while loops enable iteration. We'll see how these are implemented in C and Python, emphasizing efficiency and readability for scalable code.

## Key Concepts
- **Conditionals**: if, else if, else for decision-making based on conditions.
- **Loops**: for and while loops for repetition.
- **Best Practices**: Avoid infinite loops, use meaningful conditions, and consider loop efficiency in large-scale applications.

## C Language Section

### Conditionals
Use `if`, `else if`, `else`. Conditions evaluate to true (non-zero) or false (zero).

Syntax:
```c
if (condition) {
    // code
} else if (another_condition) {
    // code
} else {
    // code
}
```

### Loops
- **while**: Repeats while condition is true.
- **for**: Typically for counted loops.

Syntax:
```c
for (int i = 0; i < 10; i++) {
    // code
}
```

### Example Code
See `lesson.c` for examples with comments.

## Python Language Section

### Conditionals
Similar to C, but uses indentation instead of braces. Truthy/falsy values apply.

Syntax:
```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code
```

### Loops
- **while**: Repeats while condition is true.
- **for**: Iterates over iterables (lists, ranges, etc.).

Syntax:
```python
for i in range(10):
    # code
```

Python's for is more flexible for iterating over data structures.

### Example Code
See `lesson.py` for examples with comments.

## Best Practices
- In C: Be cautious with loop indices to prevent off-by-one errors.
- In Python: Use list comprehensions for concise loops when appropriate.
- Always test edge cases (e.g., empty lists, zero values).
- Write comments explaining complex logic.
- Modularize: Extract conditional blocks into functions for reusability.

## Exercises
1. **C and Python**: Write a program that loops from 1 to 100, printing "Fizz" for multiples of 3, "Buzz" for 5, "FizzBuzz" for both, else the number.
2. **Conditional**: Add a check if a number is even or odd using if-else.
3. **Comparison**: Note how Python's for loop differs from C's; discuss implications for data processing in AI models.

Compile/run your programs. Debug by stepping through loops.

## Next Steps
Day 3 will cover functions, allowing us to organize code into reusable blocks.

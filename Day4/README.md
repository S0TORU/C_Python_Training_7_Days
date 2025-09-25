# Day 4: Pointers and Memory Management in C, Data Structures in Python

## Overview
Today, we tackle memory management in C with pointers, crucial for efficient, low-level programming. In Python, we'll explore built-in data structures for handling data flexibly. These concepts are key for scalable systems and AI models.

## Key Concepts
- **Pointers in C**: Variables holding memory addresses; enable dynamic memory and efficiency.
- **Memory Management**: Allocation/deallocation to prevent leaks.
- **Data Structures in Python**: Lists, dictionaries, sets for data manipulation.

## C Language Section

### Pointers
Declare with `*`: `int *ptr;`

- `&` gets address: `ptr = &var;`
- `*` dereferences: `value = *ptr;`

### Memory Management
- `malloc()` allocates, `free()` deallocates.
- Avoid leaks: Always free allocated memory.

### Example Code
See `lesson.c` for pointer usage and dynamic arrays.

## Python Language Section

### Data Structures
- **Lists**: Mutable sequences.
- **Dictionaries**: Key-value pairs.
- **Sets**: Unique elements.
- **Tuples**: Immutable sequences.

Python handles memory automatically (garbage collection).

### Example Code
See `lesson.py` for examples.

## Best Practices
- In C: Check malloc returns, free memory, avoid dangling pointers.
- In Python: Choose appropriate data structures for performance (e.g., dict for fast lookups).
- Write tests: Ensure memory-safe code.

## Exercises
1. **C**: Implement a dynamic array using pointers and malloc.
2. **Python**: Use a dict to store user data from Day 1.
3. **Comparison**: Discuss trade-offs between manual memory management and automatic.

## Next Steps
Day 5 covers File I/O and Error Handling for persistent data and robustness.

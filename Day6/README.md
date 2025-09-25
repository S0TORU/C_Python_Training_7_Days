# Day 6: Advanced Topics - Structs and Unions in C, Classes in Python

## Overview
Today, we explore structuring data: structs/unions for C's custom types, and classes for Python's OOP.

## Key Concepts
- **Structs in C**: Group variables.
- **Unions**: Shared memory.
- **Classes in Python**: OOP with methods and attributes.

## C Language Section

### Structs
```c
struct Person {
    char name[50];
    int age;
};
```

### Unions
```c
union Data {
    int i;
    float f;
};
```

### Example Code
See `lesson.c`.

## Python Language Section

### Classes
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Example Code
See `lesson.py`.

## Best Practices
- Use structs for related data.
- Classes for encapsulation.

## Exercises
1. Define a struct/class for user data.
2. Create instances and methods.

## Next Steps
Day 7: Integration and Best Practices.

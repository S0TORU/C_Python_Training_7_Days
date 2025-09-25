# Day 5: File I/O and Error Handling

## Overview
Today, we learn to read from and write to files for data persistence, and handle errors gracefully. Robust error handling is essential for reliable systems, especially in AI and medical applications.

## Key Concepts
- **File I/O**: Opening, reading, writing, closing files.
- **Error Handling**: Detecting and responding to errors.

## C Language Section

### File I/O
Use `fopen()`, `fread()`, `fwrite()`, `fclose()` from `<stdio.h>`.

Modes: "r", "w", "a", etc.

### Error Handling
Check return values, use `errno` for details.

### Example Code
See `lesson.c`.

## Python Language Section

### File I/O
Use `open()` with context managers (`with`).

### Error Handling
Try-except blocks.

### Example Code
See `lesson.py`.

## Best Practices
- Close files properly.
- Handle exceptions.
- Validate data.

## Exercises
1. Write a program that writes user data to a file and reads it back.
2. Add error handling for file not found.

## Next Steps
Day 6: Advanced topics - Structs in C, Classes in Python.

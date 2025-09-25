#include <stdio.h>

// This program demonstrates basic variables, data types, and I/O in C.
// It reads user input for name, age, and height, then prints a formatted message.
// Best practice: Always check scanf return values in production code for error handling.

int main() {
    // Declare variables with appropriate data types
    int age;           // Integer for age
    float height;      // Float for height (single precision)
    char name[50];     // Character array for name (fixed size, watch for buffer overflows)

    // Input section: Prompt user for data
    printf("Enter your name: ");
    scanf("%s", name);  // Reads a string until whitespace

    printf("Enter your age: ");
    scanf("%d", &age);  // Note: & for address of variable

    printf("Enter your height in meters: ");
    scanf("%f", &height);

    // Output section: Display the collected information
    printf("Hello %s, you are %d years old and %.2f meters tall.\n", name, age, height);

    return 0;  // Successful execution
}

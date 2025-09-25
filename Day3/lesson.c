#include <stdio.h>

// Function prototypes (best practice in C for forward declarations)
int add(int a, int b);
long factorial(int n);

// Main function
int main() {
    // Example 1: Simple function call
    int sum = add(5, 3);
    printf("5 + 3 = %d\n", sum);

    // Example 2: Recursive function
    int num = 5;
    long fact = factorial(num);
    printf("Factorial of %d is %ld\n", num, fact);

    // Example 3: Modular I/O (refactoring Day 1 idea)
    // Note: In C, functions help organize code
    printf("Modular example: ");
    print_hello();

    return 0;
}

// Function definitions
int add(int a, int b) {
    return a + b;  // Simple addition
}

long factorial(int n) {
    if (n <= 1) {
        return 1;  // Base case
    } else {
        return n * factorial(n - 1);  // Recursive call
    }
}

void print_hello() {
    printf("Hello from a function!\n");
}

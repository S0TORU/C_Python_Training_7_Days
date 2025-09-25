#include <stdio.h>

// This program demonstrates control structures in C: conditionals and loops.
// It includes examples of if-else and for/while loops.
// Best practice: Use meaningful variable names and avoid magic numbers.

int main() {
    // Example 1: Conditional - Check if a number is even or odd
    int num = 7;  // Example number
    if (num % 2 == 0) {
        printf("%d is even.\n", num);
    } else {
        printf("%d is odd.\n", num);
    }

    // Example 2: Loop - Print numbers from 1 to 10 using for loop
    printf("Numbers from 1 to 10:\n");
    for (int i = 1; i <= 10; i++) {
        printf("%d ", i);
    }
    printf("\n");

    // Example 3: While loop - Simple countdown
    int countdown = 5;
    while (countdown > 0) {
        printf("Countdown: %d\n", countdown);
        countdown--;
    }
    printf("Blast off!\n");

    // Example 4: FizzBuzz logic in a loop (from exercises)
    printf("FizzBuzz from 1 to 20:\n");
    for (int i = 1; i <= 20; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            printf("FizzBuzz ");
        } else if (i % 3 == 0) {
            printf("Fizz ");
        } else if (i % 5 == 0) {
            printf("Buzz ");
        } else {
            printf("%d ", i);
        }
    }
    printf("\n");

    return 0;
}

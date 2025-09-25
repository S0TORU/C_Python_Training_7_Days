#include <stdio.h>
#include <stdlib.h>

// This program demonstrates pointers and memory management in C.
// Best practice: Always check allocations and free memory to prevent leaks.

int main() {
    // Example 1: Basic pointers
    int var = 10;
    int *ptr = &var;  // Pointer to var
    printf("Value of var: %d\n", var);
    printf("Address of var: %p\n", (void*)&var);
    printf("Value via pointer: %d\n", *ptr);

    // Modify via pointer
    *ptr = 20;
    printf("Modified var: %d\n", var);

    // Example 2: Dynamic memory allocation
    int *dynamic_array = (int*)malloc(5 * sizeof(int));  // Allocate for 5 ints
    if (dynamic_array == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Fill and print
    for (int i = 0; i < 5; i++) {
        dynamic_array[i] = i * 10;
        printf("dynamic_array[%d] = %d\n", i, dynamic_array[i]);
    }

    // Free memory
    free(dynamic_array);
    printf("Memory freed.\n");

    // Example 3: Pointer to function (advanced)
    // Note: For simplicity, just showing concept

    return 0;
}

#include <stdio.h>
#include <stdlib.h>

// File I/O and error handling in C.

int main() {
    // Writing to file
    FILE *file = fopen("example.txt", "w");
    if (file == NULL) {
        perror("Error opening file for writing");
        return 1;
    }
    fprintf(file, "Hello, World!\n");
    fprintf(file, "This is a test file.\n");
    fclose(file);

    // Reading from file
    file = fopen("example.txt", "r");
    if (file == NULL) {
        perror("Error opening file for reading");
        return 1;
    }
    char buffer[100];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("Read: %s", buffer);
    }
    fclose(file);

    return 0;
}

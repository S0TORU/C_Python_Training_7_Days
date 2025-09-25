#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Integrated example: Struct, functions, file I/O, error handling.

struct User {
    char name[50];
    int age;
};

void save_user(struct User u) {
    FILE *f = fopen("user.txt", "w");
    if (f == NULL) {
        perror("Save failed");
        return;
    }
    fprintf(f, "%s %d\n", u.name, u.age);
    fclose(f);
}

struct User load_user() {
    struct User u;
    FILE *f = fopen("user.txt", "r");
    if (f == NULL) {
        perror("Load failed");
        strcpy(u.name, "Error");
        u.age = -1;
        return u;
    }
    fscanf(f, "%s %d", u.name, &u.age);
    fclose(f);
    return u;
}

int main() {
    struct User u = {"Bob", 25};
    save_user(u);
    struct User loaded = load_user();
    printf("Loaded: %s, %d\n", loaded.name, loaded.age);
    return 0;
}

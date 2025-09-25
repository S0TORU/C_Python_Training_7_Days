#include <stdio.h>
#include <string.h>

// Structs and unions in C.

struct Person {
    char name[50];
    int age;
};

union Data {
    int i;
    float f;
};

int main() {
    // Struct
    struct Person p;
    strcpy(p.name, "Alice");
    p.age = 30;
    printf("Person: %s, %d\n", p.name, p.age);

    // Union
    union Data d;
    d.i = 10;
    printf("Union as int: %d\n", d.i);
    d.f = 3.14;
    printf("Union as float: %f\n", d.f);

    return 0;
}

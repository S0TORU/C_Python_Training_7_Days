# Classes in Python.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}, {self.age} years old."

# Usage
p = Person("Alice", 30)
print(p.greet())

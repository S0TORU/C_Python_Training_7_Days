# Integrated example: Class, functions, file I/O, error handling.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self, filename):
        try:
            with open(filename, "w") as f:
                f.write(f"{self.name} {self.age}\n")
        except IOError as e:
            print(f"Save failed: {e}")

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, "r") as f:
                data = f.read().strip().split()
                return cls(data[0], int(data[1]))
        except (IOError, ValueError) as e:
            print(f"Load failed: {e}")
            return cls("Error", -1)

# Usage
u = User("Bob", 25)
u.save("user.txt")
loaded = User.load("user.txt")
print(f"Loaded: {loaded.name}, {loaded.age}")

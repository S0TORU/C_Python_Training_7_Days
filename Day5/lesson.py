# File I/O and error handling in Python.

try:
    # Writing to file
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")

    # Reading from file
    with open("example.txt", "r") as file:
        content = file.read()
        print("Read content:")
        print(content)

except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print(f"I/O error: {e}")

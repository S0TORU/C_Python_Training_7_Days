# This program demonstrates data structures in Python.
# Python handles memory automatically, focusing on usage.
# Best practice: Choose structures based on use case for efficiency.

# Example 1: Lists - Mutable sequences
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
my_list.append(6)  # Add element
print("After append:", my_list)
print("Sliced [1:4]:", my_list[1:4])

# Example 2: Dictionaries - Key-value pairs
my_dict = {"name": "Alice", "age": 30, "city": "NYC"}
print("Dict:", my_dict)
print("Age:", my_dict["age"])
my_dict["job"] = "Engineer"  # Add key-value
print("Updated dict:", my_dict)

# Example 3: Sets - Unique elements
my_set = {1, 2, 2, 3}  # Duplicates removed
print("Set:", my_set)
my_set.add(4)
print("After add:", my_set)

# Example 4: Tuples - Immutable
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)
# my_tuple[0] = 10  # Would error - immutable

# Example 5: List comprehension (efficient data manipulation)
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Note: For large data, consider performance; e.g., dict for O(1) lookups

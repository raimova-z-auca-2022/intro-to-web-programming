# Exercise 1: Working with Lists

# Task 1: Basic List Operations
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
numbers.reverse()
numbers.sort()
print("Updated List:", numbers)

# Task 2: List Slicing and Indexing
print("First 3 elements:", numbers[:3])
print("Last 2 elements:", numbers[-2:])
print("Reversed List (without modifying):", numbers[::-1])

# Exercise 2: Working with Dictionaries

# Task 3: Basic Dictionary Operations
student = {"name": "Alice", "age": 22, "grade": "A"}
student["subject"] = "Math"
student["grade"] = "A+"
student.pop("age")
print("Dictionary:", student)

# Print all keys and values
print("Keys:", student.keys())
print("Values:", student.values())

# Exercise 3: Working with Sets

# Task 4: Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))

# Exercise 4: Working with Tuples

# Task 5: Tuple Methods
colors = ("red", "blue", "green", "red", "yellow")

print("Index of 'green':", colors.index("green"))
print("Count of 'red':", colors.count("red"))

# Challenge Task: Nested Data Structures

# Task 6: Working with Nested Lists and Dictionaries
company = {
    "employees": [
        {"name": "Alice", "position": "Developer", "salary": 60000},
        {"name": "Bob", "position": "Designer", "salary": 50000},
        {"name": "Charlie", "position": "Manager", "salary": 70000}
    ]
}

# Add a new employee
company["employees"].append({"name": "David", "position": "Intern", "salary": 30000})

# Print names of all employees
for employee in company["employees"]:
    print("Employee Name:", employee["name"])

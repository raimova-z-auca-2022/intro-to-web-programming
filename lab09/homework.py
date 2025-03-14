try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range.")

try:
    my_dict = {"name": "John"}
    print(my_dict["age"])
except KeyError:
    print("Key not found.")

try:
    result = "hello" + 5
except TypeError:
    print("Cannot add string and integer.")

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print("Error:", e)

class NegativeNumberError(Exception):
    pass

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    return number ** 0.5

try:
    print(square_root(-4))
except NegativeNumberError as e:
    print("Error:", e)

try:
    print("Trying block executed")
except:
    print("Exception occurred")
else:
    print("No exception occurred")
finally:
    print("Finally block executed")

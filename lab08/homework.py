# 1. Defining a Function
def greet():
    print("Hello, welcome to functions in Python!")

greet()

# 2. Function Parameters
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 3))

# 3. Default Parameters
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()
greet_user("Zarina")

# 4. Returning Values
def square(num):
    return num ** 2

print(square(4))

# 5. Multiple Return Values
def get_name_and_age():
    return "Zarina", 20

name, age = get_name_and_age()
print(name, age)

# 6. Variable-Length Arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))

def display_info(**info):
    print(info)

display_info(name="Zarina", age=20, country="Kyrgyzstan")

# 7. Lambda Functions
double = lambda x: x * 2
print(double(5))

# 8. Scope of Variables
x = 10  # Global variable

def access_global():
    global x
    x = 20  # Modifying global variable
    print("Inside function:", x)

access_global()
print("Outside function:", x)

# 9. Recursion (Fibonacci)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

# 10. Docstrings
def is_prime(n):
    """This function checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))

# Practice Exercises
# Square of a number
def square_num(n):
    return n ** 2

print(square_num(5))

# Sum of a list of numbers
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(7))

# Check if a number is prime
print(is_prime(17))

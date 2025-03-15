# Class and Object
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year})")

# Creating an object
car1 = Car("Toyota", "Camry", 2020)
car1.display_info()


# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery):
        super().__init__(brand, model, year)
        self.battery = battery

    def display_info(self):
        super().display_info()
        print(f"Battery: {self.battery} kWh")


# Inheritance Example
car2 = ElectricCar("Tesla", "Model S", 2022, 100)
car2.display_info()


# Polymorphism
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Polymorphism Example
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()


# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount


# Encapsulation Example
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Balance:", account.get_balance())


# Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")


# Abstraction Example
car = Car()
car.start_engine()
motorcycle = Motorcycle()
motorcycle.start_engine()


# Method Overriding
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")


# Method Overriding Example
child = Child()
child.show()


# Multiple Inheritance
class A:
    def method_a(self):
        print("Method from class A")

class B:
    def method_b(self):
        print("Method from class B")

class C(A, B):
    pass


# Multiple Inheritance Example
obj = C()
obj.method_a()
obj.method_b()

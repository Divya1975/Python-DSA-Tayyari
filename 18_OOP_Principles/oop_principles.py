# OOP Principles Demonstration in Python

# 1. Polymorphism – Method Overriding
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()
make_sound(dog)  # Output: Dog barks
make_sound(cat)  # Output: Cat meows

# ------------------------------------------

# 2. Inheritance
class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def drive(self):
        print("Driving the car")

car = Car()
car.start_engine()  # Inherited method
car.drive()

# ------------------------------------------

# 3. Encapsulation
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account("Divya", 1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500

# ------------------------------------------

# 4. Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print("Area of circle:", circle.area())

#  OOP Fundamentals – Concepts Demonstration

# Class and Object
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

# Creating Object
s1 = Student("Divya", 101)
s1.display()

# Encapsulation Example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Divya", 5000)
acc.deposit(1500)
print("Balance:", acc.get_balance())

# Inheritance Example
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

# Polymorphism Example
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Square(Shape):
    def area(self):
        return 4 * 4

shapes = [Circle(), Square()]
for shape in shapes:
    print("Area:", shape.area())

# Class method & static method
class Demo:
    college_name = "MITS"

    @classmethod
    def show_college(cls):
        print("College:", cls.college_name)

    @staticmethod
    def greet():
        print("Welcome to OOP world!")

Demo.show_college()
Demo.greet()

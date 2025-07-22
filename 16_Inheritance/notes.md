#  Inheritance in Python

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). It promotes **code reusability** and supports **OOP principles** like **extensibility and modularity**.

---

##  Key Concepts:

###  Parent Class / Base Class
The class being inherited from.

###  Child Class / Derived Class
The class that inherits from the parent.

###  `super()` Keyword
Used to call methods/constructors from the parent class.

---

##  Types of Inheritance:

| Type                   | Description                              |
|------------------------|------------------------------------------|
| Single Inheritance     | One child inherits from one parent       |
| Multiple Inheritance   | One child inherits from multiple parents |
| Multilevel Inheritance | Child of a child inherits a parent       |
| Hierarchical Inheritance | Multiple children from one parent     |

---

##  Example

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Single Inheritance
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Inherited method
d.bark()

##  Use of super()
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)  # calling parent constructor
        self.roll = roll
##  Advantages
Code Reusability

Improved Modularity

DRY Principle (Don't Repeat Yourself)

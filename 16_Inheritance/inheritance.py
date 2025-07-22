# inheritance.py

#  Example 1: Single Inheritance
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Inherited from Animal
d.bark()


#  Example 2: Multilevel Inheritance
class Grandparent:
    def show_grandparent(self):
        print("This is the grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("This is the parent")

class Child(Parent):
    def show_child(self):
        print("This is the child")

c = Child()
c.show_grandparent()
c.show_parent()
c.show_child()


#  Example 3: Multiple Inheritance
class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Duck quacks")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()


#  Example 4: Using super() to call parent constructor
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        super().display()
        print(f"Roll: {self.roll}")

s = Student("Divya", 101)
s.display()

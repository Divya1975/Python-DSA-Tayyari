#  Polymorphism in Python

## What is Polymorphism?
Polymorphism means “many forms”.  
In Python, it refers to the ability of different objects to respond to the same function call in different ways.

---

##  Types of Polymorphism

## 1. **Duck Typing (Pythonic Polymorphism)**
If an object walks like a duck and quacks like a duck — it’s treated like a duck.

## 
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

def make_sound(animal):
    animal.sound()

make_sound(Cat())   # Meow
make_sound(Dog())   # Woof

## 2. Method Overriding (Runtime Polymorphism)
Happens when a child class redefines a method from the parent class.
class Shape:
    def area(self):
        print("Area is not defined")

class Circle(Shape):
    def area(self):
        print("Area of circle = πr²")

circle = Circle()
circle.area()  # Area of circle = πr²

##  Python does NOT support Method Overloading (Compile-time Polymorphism)
But you can simulate it using default arguments:
def add(a, b=0, c=0):
    return a + b + c

print(add(2))        # 2
print(add(2, 3))     # 5
print(add(2, 3, 4))  # 9

## Key Takeaways:
Python relies on dynamic typing for polymorphism.

Method Overriding enables flexibility in OOP design.

Method Overloading is not natively supported — but can be simulated.

## Real-Life Example:
A single function draw() can behave differently depending on whether it is applied to a Circle, Rectangle, or Triangle.

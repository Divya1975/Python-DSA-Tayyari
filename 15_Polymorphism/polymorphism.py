# polymorphism.py

#  Duck Typing Example
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def start_flying(obj):
    obj.fly()

start_flying(Bird())      # Bird is flying
start_flying(Airplane())  # Airplane is flying


#  Method Overriding Example
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Animal(), Dog(), Cat()]
for animal in animals:
    animal.speak()


#  Simulated Method Overloading using default arguments
def greet(name=None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello!")

greet()           # Hello!
greet("Divya")    # Hello, Divya!


#  Polymorphism with functions and classes
class Circle:
    def area(self):
        return "Area = πr²"

class Rectangle:
    def area(self):
        return "Area = length × width"

def print_area(shape):
    print(shape.area())

print_area(Circle())     # Area = πr²
print_area(Rectangle())  # Area = length × width

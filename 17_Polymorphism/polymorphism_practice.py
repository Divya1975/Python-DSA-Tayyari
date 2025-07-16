# polymorphism_practice.py

# Q1. Use polymorphism to define a function that accepts different types of pets

class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

def pet_sound(pet):
    print(pet.sound())

pet_sound(Cat())  # Output: Meow
pet_sound(Dog())  # Output: Bark


# Q2. Method Overriding example
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving on the road")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing on water")

vehicles = [Vehicle(), Car(), Boat()]
for v in vehicles:
    v.move()


# Q3. Demonstrate Duck Typing with a custom function

class Developer:
    def code(self):
        print("Developer is writing Python code")

class Designer:
    def code(self):
        print("Designer is prototyping in Figma")

def start_work(person):
    person.code()

start_work(Developer())  # Output: Developer is writing Python code
start_work(Designer())   # Output: Designer is prototyping in Figma

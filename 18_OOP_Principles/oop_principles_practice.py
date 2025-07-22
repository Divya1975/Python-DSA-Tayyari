# Practice: Polymorphism
class Bird:
    def sound(self):
        print("Birds make sounds")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks")

def make_bird_sound(bird):
    bird.sound()

make_bird_sound(Sparrow())
make_bird_sound(Parrot())

# ------------------------------------------

# Practice: Inheritance
class Parent:
    def show_love(self):
        print("Parent shows love ❤️")

class Child(Parent):
    def play(self):
        print("Child plays with toys")

c = Child()
c.show_love()
c.play()

# ------------------------------------------

# Practice: Encapsulation
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade  # private

    def get_grade(self):
        return self.__grade

    def improve_grade(self, bonus):
        self.__grade += bonus

s = Student("Riya", 75)
print(s.get_grade())
s.improve_grade(5)
print(s.get_grade())

# ------------------------------------------

# Practice: Abstraction
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def operate(self):
        pass

class Laptop(Device):
    def operate(self):
        print("Laptop running code")

class Printer(Device):
    def operate(self):
        print("Printer printing document")

for d in [Laptop(), Printer()]:
    d.operate()

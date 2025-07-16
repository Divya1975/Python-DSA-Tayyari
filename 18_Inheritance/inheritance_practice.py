# inheritance_practice.py

# Q1. Single Inheritance: Create a class Vehicle with a method run(). Inherit it into Car and add method drive().

class Vehicle:
    def run(self):
        print("Vehicle is running")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

car = Car()
car.run()
car.drive()


# Q2. Multilevel Inheritance: Create classes: Device → Computer → Laptop

class Device:
    def info(self):
        print("This is an electronic device.")

class Computer(Device):
    def compute(self):
        print("Can perform computations.")

class Laptop(Computer):
    def portability(self):
        print("Easy to carry.")

l = Laptop()
l.info()
l.compute()
l.portability()


# Q3. Multiple Inheritance: Create class Writer and Artist, inherit into ContentCreator

class Writer:
    def write(self):
        print("Writes content")

class Artist:
    def draw(self):
        print("Creates digital art")

class ContentCreator(Writer, Artist):
    def publish(self):
        print("Publishes on social media")

cc = ContentCreator()
cc.write()
cc.draw()
cc.publish()


# Q4. Use of super() to call parent class constructor

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def display(self):
        print(f"Name: {self.name}, Language: {self.language}")

dev = Developer("Divya", "Python")
dev.display()

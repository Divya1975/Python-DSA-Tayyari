#  OOP Fundamentals Practice Problems

# 1. Create a class `Book` with title, author, and pages
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"📖 '{self.title}' by {self.author} ({self.pages} pages)")

b1 = Book("The Alchemist", "Paulo Coelho", 197)
b1.show_info()

# 2. Create a class `Rectangle` with methods to calculate area and perimeter
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(5, 3)
print("Area:", r.area())
print("Perimeter:", r.perimeter())

# 3. Create a class `Employee` and display name and salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"👩‍💻 {self.name} earns ₹{self.salary}/month")

e1 = Employee("Divya", 50000)
e1.display()

# 4. Inheritance Practice: Base class `Vehicle`, derived class `Car`
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is moving...")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving smoothly 🚗")

c = Car("Hyundai")
c.drive()

# 5. Polymorphism Practice: Multiple shapes with area() method
class Triangle:
    def area(self):
        return 0.5 * 4 * 3

class Circle:
    def area(self):
        return 3.14 * 3 * 3

shapes = [Triangle(), Circle()]
for shape in shapes:
    print("Area:", shape.area())

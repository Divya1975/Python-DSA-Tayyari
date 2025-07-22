# Practice problems for methods and members

class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius


c1 = Circle(5)
print("Area:", c1.area())
print("Circumference:", c1.circumference())


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @staticmethod
    def info():
        print("This class converts Celsius to Fahrenheit.")


t1 = Temperature(30)
print("Fahrenheit:", t1.to_fahrenheit())
Temperature.info()

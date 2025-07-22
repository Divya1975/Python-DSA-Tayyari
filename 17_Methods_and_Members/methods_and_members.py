# Demonstrating class members and methods

class Student:
    college = "MITS"  # class variable (shared by all)

    def __init__(self, name, roll):
        self.name = name         # instance variable
        self.roll = roll

    def introduce(self):  # instance method
        print(f"Hi, I'm {self.name} and my roll number is {self.roll}.")

    @classmethod
    def college_info(cls):  # class method
        print(f"College: {cls.college}")

    @staticmethod
    def say_hello():  # static method
        print("Hello from the Student class!")


# Creating objects
s1 = Student("Divya", 101)
s2 = Student("Raghav", 102)

s1.introduce()
s2.introduce()

Student.college_info()
Student.say_hello()

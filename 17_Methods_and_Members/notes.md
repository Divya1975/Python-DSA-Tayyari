#  19 – Methods and Members in Python Classes

---

##  Class Members
Class members refer to:
- **Attributes** (variables)
- **Methods** (functions) defined inside a class


class Student:
    college = "MITS"  # class variable 

   def __init__(self, name):
        self.name = name  # instance variable

  def greet(self):
        print(f"Hi, I'm {self.name} from {Student.college}")

## Types of Members
| Type               | Description                           | Accessed via    |
| ------------------ | ------------------------------------- | --------------- |
| Instance Variables | Unique to each object                 | `self.var`      |
| Class Variables    | Shared among all objects              | `Class.var`     |
| Instance Methods   | Work with object data (`self`)        | `obj.method()`  |
| Class Methods      | Work with class data (`cls`)          | `@classmethod`  |
| Static Methods     | Independent logic, no `self` or `cls` | `@staticmethod` |

## Special Methods (Dunder methods)
These methods begin and end with double underscores (__):

__init__ – constructor

__str__ – string representation

__len__ – custom length

def __str__(self):
    return f"Student: {self.name}"

## When to Use What?
Use instance methods when you want to operate on object data

Use class methods when working with the class itself (e.g., factory methods)

Use static methods for utility/helper logic



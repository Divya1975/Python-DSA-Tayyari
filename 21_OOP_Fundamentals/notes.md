###  OOP Fundamentals – Notes

---

####  What is Object-Oriented Programming (OOP)?
OOP is a programming paradigm based on the concept of **“objects”**, which can contain **data (attributes)** and **functions (methods)**.

---

####  Key OOP Concepts

| Concept         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Class**       | Blueprint for creating objects. Defines attributes and behaviors.           |
| **Object**      | Instance of a class.                                                         |
| **Encapsulation** | Hiding internal data using access modifiers (`private`, `protected`).     |
| **Abstraction** | Showing only essential features. Hides complexity.                          |
| **Inheritance** | One class acquires the properties and behavior of another.                  |
| **Polymorphism**| Same method behaves differently in different classes.                       |

---

####  Structure of a Class in Python

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

  def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h")

# Object creation
c1 = Car("BMW", 120)
c1.drive()

---

####  Access Modifiers
| Modifier     | Meaning               | Syntax Example       |
|--------------|------------------------|-----------------------|
| `public`     | Accessible everywhere  | `self.name`           |
| `protected`  | Accessible in subclasses | `self._name`        |
| `private`    | Accessible only in class | `self.__name`       |

---

####  Method Types
- **Instance Method** – Works with instance data.  
- **Class Method** – Works with class data. Defined using `@classmethod`.  
- **Static Method** – Doesn’t access class or instance. Defined using `@staticmethod`.

---

####  Summary
Object-Oriented Programming helps to:
- Organize code better.
- Promote code reuse.
- Improve scalability and maintenance.

 _“Think in objects, not functions.”_

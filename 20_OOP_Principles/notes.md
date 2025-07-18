##2. I – Inheritance
Enables a class to use properties & methods of another class.

Promotes code reusability.

Types:
Single, Multiple, Multilevel, Hierarchical, Hybrid OOP Principles – The Pillars of Object-Oriented Programming

OOP (Object-Oriented Programming) is built on **4 main principles**, often remembered as **PIE-A**:

---

## 1. P – Polymorphism**
- *Poly* = many, *morph* = forms
- Allows objects to behave differently based on context.
- 🔁 Method Overriding (runtime) & Method Overloading (compile-time)

### Example:

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Dog()
a.sound()  # Output: Bark

## 2. I – Inheritance
Enables a class to use properties & methods of another class.

Promotes code reusability.

Types:
Single, Multiple, Multilevel, Hierarchical, Hybrid

## 3. E – Encapsulation
Bundling data and methods that work on data within one unit (class).

Hides internal state using private/protected members.

Achieved using _ or __ before variable names.

 class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

   def deposit(self, amount):
        self.__balance += amount

## 4. A – Abstraction
Hides unnecessary details and shows only relevant features.

Implemented using abstract base classes or interfaces.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

## Summary Table:
| Principle     | What it Means     | Benefits                 |
| ------------- | ----------------- | ------------------------ |
| Polymorphism  | Many forms        | Flexibility              |
| Inheritance   | Class reuse       | Code reusability         |
| Encapsulation | Data hiding       | Security, Modularity     |
| Abstraction   | Hiding complexity | Focus on essential logic |



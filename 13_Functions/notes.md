## What is a Function?
A function is a reusable block of code that performs a specific task.
Functions help break programs into smaller, manageable, and reusable parts.

## Types of Functions
Built-in Functions: print(), len(), sum(), etc.
User-defined Functions: Defined using def keyword.
Lambda Functions: Anonymous, single-line functions.

## Defining and Calling a Function
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

## Function with Parameters
def add(a, b):
    return a + b

result = add(5, 3)  # Output: 8

## Default Parameters
def greet(name="User"):
    print("Hello,", name)

greet()          # Output: Hello, User
greet("Divya")   # Output: Hello, Divya

## Keyword vs Positional Arguments
def display(name, age):
    print(name, age)

display("Divya", 20)               # Positional
display(age=20, name="Divya")      # Keyword

## Return Statement
def square(x):
    return x * x

print(square(4))  # Output: 16

## Variable-Length Arguments 
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))  # Output: 10

## Lambda Function
square = lambda x: x * x
print(square(5))  # Output: 25

## Scope of Variables
Local: Inside the function only.
Global: Declared outside the function.

 x = 10  # Global

def show():
    x = 5  # Local
    print(x)

show()   # Output: 5
print(x) # Output: 10

## Recursion (Basic)
A function calling itself .

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


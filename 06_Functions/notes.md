# 🔧 Python Functions - Notes

##  What is a Function?
A **function** is a reusable block of code that performs a specific task. Functions help in organizing code, reducing repetition, and improving readability.

---

##  Defining a Function

def function_name(parameters):
    # function body
    return value
    
    
## def — keyword to define a function

function_name — name of your function

parameters — optional inputs to the function

return — optional, used to send back a result

def greet(name):
    return "Hello " + name

print(greet("Divya"))

## Types of Functions
Built-in Functions
➤ Already provided by Python
➤ Examples: print(), len(), sum(), max()

User-defined Functions
➤ Created by the programmer using def

## Function Components
Parameters: Inputs to the function

Return Statement: Gives back output from the function

Arguments: Actual values passed when calling the function

## Types of Parameters
Required: Must be passed

Default: Has a default value

Keyword: Passed with key=value format

Arbitrary: *args and **kwargs

## Difference Between print() vs return
print() displays the result to the user

return sends data back to the caller (useful for logic)

## Default Parameters
You can assign default values to parameters.

def greet(name="Guest"):
    print("Hello,", name)

greet("Divya")  # Output: Hello, Divya
greet()         # Output: Hello, Guest

## *args and **kwargs
*args allows you to pass multiple positional arguments

**kwargs allows you to pass multiple keyword arguments

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Divya", age=20)

## Recursion
A function that calls itself.

Must have a base case to avoid infinite recursion.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

## Lambda Functions
Anonymous function created using lambda keyword.

Good for short one-liners.

square = lambda x: x * x
print(square(4))  # Output: 16

## Docstrings
Used to describe what a function does.

def add(a, b):
    """Returns the sum of a and b"""
    return a + b

print(add.__doc__)

## Scope of Variables
Local Scope: Variables declared inside a function

Global Scope: Variables declared outside any function

x = 5  # Global

def show():
    x = 10  # Local
    print("Inside:", x)

show()         # Inside: 10
print("Outside:", x)  # Outside: 5







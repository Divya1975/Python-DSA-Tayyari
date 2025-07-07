# 🧠 Basic Function
def greet():
    print("Hello! Welcome to Python Functions.")

greet()


# ✅ Function with Parameters
def add(a, b):
    return a + b

print("Sum is:", add(3, 5))


# 🎯 Function with Default Parameter
def welcome(name="Guest"):
    print("Welcome,", name)

welcome("Divya")
welcome()


# 🌀 Function with Return Statement
def multiply(x, y):
    product = x * y
    return product

result = multiply(4, 6)
print("Multiplication Result:", result)


# 🔄 Function with *args
def total_sum(*args):
    return sum(args)

print("Total Sum:", total_sum(10, 20, 30))


# 🔍 Function with **kwargs
def display_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_profile(name="Divya", age=20, course="Python DSA")


# 🧬 Lambda Function
square = lambda n: n * n
print("Square of 5:", square(5))


# ♻️ Recursive Function (Factorial)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

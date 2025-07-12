# 1. Basic Function
def greet():
    print("Hello, welcome to Python DSA!")

greet()

# 2. Function with Parameters
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

# 3. Default Parameter
def welcome(name="Coder"):
    print("Welcome,", name)

welcome()
welcome("Divya")

# 4. Keyword Arguments
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce(age=21, name="Divya")

# 5. Return Statement
def multiply(x, y):
    return x * y

result = multiply(4, 6)
print("Multiplication:", result)

# 6. Variable Length Arguments
def total_marks(*marks):
    return sum(marks)

print("Total:", total_marks(80, 90, 85, 95))

# 7. Lambda Function
square = lambda x: x * x
print("Square of 5:", square(5))

# 8. Scope Example
global_var = "Python"

def show_scope():
    local_var = "DSA"
    print("Inside function:", local_var)

show_scope()
print("Outside function:", global_var)

# 1. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# 2. Fibonacci using recursion
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("6th Fibonacci number:", fibonacci(6))


# 3. Sum of natural numbers
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

print("Sum of first 5 natural numbers:", sum_natural(5))


# 4. Reverse a string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print("Reverse of 'python':", reverse_string("python"))


# 5. Power of a number (x^n)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print("2^4 =", power(2, 4))

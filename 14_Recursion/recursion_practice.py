# Q1. Find GCD (Greatest Common Divisor) using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("GCD of 24 and 18:", gcd(24, 18))


# Q2. Find the nth term of the Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("8th Fibonacci number:", fibonacci(8))


# Q3. Find the sum of digits of a number
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print("Sum of digits of 1234:", sum_of_digits(1234))


# Q4. Check if a string is a palindrome using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'hello' a palindrome?", is_palindrome("hello"))


# Q5. Calculate the product of two numbers using recursion (without using *)
def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)

print("Product of 4 and 3:", multiply(4, 3))

# Q1. Write a function to find the factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))

# Q2. Write a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))
print("Is 12 prime?", is_prime(12))

# Q3. Write a function to reverse a string
def reverse_string(s):
    return s[::-1]

print("Reversed: ", reverse_string("Python"))

# Q4. Write a function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print("Vowels in 'Hello World':", count_vowels("Hello World"))

# Q5. Write a function that returns the maximum of 3 numbers
def max_of_three(a, b, c):
    return max(a, b, c)

print("Max of (3, 7, 2):", max_of_three(3, 7, 2))

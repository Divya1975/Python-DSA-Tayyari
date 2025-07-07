# Q1️⃣: Function to find maximum of three numbers
def find_max(a, b, c):
    return max(a, b, c)

print("Max of 5, 12, 7:", find_max(5, 12, 7))


# Q2️⃣: Function to check if a number is even or odd
def is_even(num):
    return num % 2 == 0

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))


# Q3️⃣: Function to calculate the square of each number in a list
def square_list(numbers):
    return [n ** 2 for n in numbers]

print("Squares:", square_list([2, 4, 6]))


# Q4️⃣: Function to count vowels in a string
def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in string if ch in vowels)

print("Vowel count in 'Hello World':", count_vowels("Hello World"))


# Q5️⃣: Function to reverse a string
def reverse_string(s):
    return s[::-1]

print("Reverse of 'Python':", reverse_string("Python"))


# Q6️⃣: Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 17 prime?", is_prime(17))
print("Is 20 prime?", is_prime(20))


# Q7️⃣: Function to print a greeting message multiple times
def repeat_greeting(name, times):
    for _ in range(times):
        print(f"Hello, {name}!")

repeat_greeting("Divya", 3)

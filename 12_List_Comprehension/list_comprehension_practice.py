# list_comprehension_practice.py

# Q1. Generate a list of all even numbers between 1 and 50
evens = [x for x in range(1, 51) if x % 2 == 0]
print("Even numbers from 1 to 50:", evens)

# Q2. Get squares of numbers from 1 to 20 that are divisible by 3
squares = [x**2 for x in range(1, 21) if x % 3 == 0]
print("Squares of numbers divisible by 3:", squares)

# Q3. Extract vowels from a string
text = "List Comprehensions Are Powerful"
vowels = [ch for ch in text if ch.lower() in "aeiou"]
print("Vowels in string:", vowels)

# Q4. Convert a list of strings to lowercase and remove whitespace
raw = [" Apple ", " BANANA", " Cherry "]
cleaned = [word.strip().lower() for word in raw]
print("Cleaned list:", cleaned)

# Q5. Find all numbers from 1 to 100 that are divisible by both 5 and 7
special_nums = [x for x in range(1, 101) if x % 5 == 0 and x % 7 == 0]
print("Divisible by 5 & 7:", special_nums)

# Q6. Create a list of (number, square) tuples for numbers from 1 to 10
num_squares = [(x, x**2) for x in range(1, 11)]
print("Number and its square:", num_squares)

# Q7. Flatten a 2D list using list comprehension
matrix = [[10, 20], [30, 40], [50, 60]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# Q8. List comprehension with if-else: Replace negative numbers with 0
nums = [5, -3, 8, -1, 0, -7]
no_negatives = [x if x >= 0 else 0 for x in nums]
print("Without negatives:", no_negatives)

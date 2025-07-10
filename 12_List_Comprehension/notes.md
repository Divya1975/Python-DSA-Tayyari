# 📝 List Comprehension in Python

## ✅ What is List Comprehension?
List comprehension is a **concise way** to create lists using a single line of code.

squares = [x**2 for x in range(5)]
It’s faster and more readable than using traditional for loops.

## Basic Syntax
[expression for item in iterable if condition]
## Example:
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

## With Loops vs List Comprehension
#Traditional Way:
squares = []
for x in range(5):
    squares.append(x**2)
#Using List Comprehension:
squares = [x**2 for x in range(5)]

## With Conditions
# Only even numbers
evens = [x for x in range(20) if x % 2 == 0]
# Numbers divisible by both 2 and 3
divisible = [x for x in range(30) if x % 2 == 0 and x % 3 == 0]

## Nested Loops in List Comprehension
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]

## With String/Lists
text = "hello"
upper_chars = [char.upper() for char in text]
words = ["apple", "banana", "kiwi"]
lengths = [len(word) for word in words]

## Notes:
You can use if-else inside list comprehension:
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
Use only when it improves readability.

## Real Use Cases
Filtering

Transforming

Flattening nested lists

Cleaning data (strip, lowercase, etc.)

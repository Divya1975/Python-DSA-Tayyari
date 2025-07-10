# list_comprehension.py

# 1. Simple list of squares
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# 2. List of even numbers
evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", evens)

# 3. Convert all characters to uppercase
text = "python"
upper_chars = [char.upper() for char in text]
print("Uppercase letters:", upper_chars)

# 4. List of words and their lengths
words = ["apple", "banana", "kiwi"]
lengths = [len(word) for word in words]
print("Lengths of words:", lengths)

# 5. If-else in list comprehension
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print("Even/Odd labels:", labels)

# 6. Flatten a 2D list using nested loop
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened list:", flattened)

# 7. Filter names that start with 'A'
names = ["Ankit", "Divya", "Aarav", "Neha"]
a_names = [name for name in names if name.startswith("A")]
print("Names starting with A:", a_names)

# 8. Remove spaces and lowercase words
messy = [" Hello ", " WorLD ", " PYTHON "]
cleaned = [word.strip().lower() for word in messy]
print("Cleaned list:", cleaned)

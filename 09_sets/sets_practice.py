# sets_practice.py

# Q1. Remove duplicates from a list using set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)

# Q2. Find common elements in two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print("Common elements:", common)

# Q3. Check if a list has duplicates
def has_duplicates(lst):
    return len(lst) != len(set(lst))

sample = [1, 2, 2, 3, 4]
print("Has duplicates?", has_duplicates(sample))

# Q4. Get all unique characters from a sentence
sentence = "learning python is fun"
unique_chars = set(sentence.replace(" ", ""))
print("Unique characters in sentence:", unique_chars)

# Q5. Use set operations
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A - B:", A - B)
print("Symmetric Difference:", A ^ B)

# Q6. Set membership test
items = {"pen", "pencil", "eraser"}
print("Is 'pen' available?", "pen" in items)
print("Is 'scale' available?", "scale" in items)

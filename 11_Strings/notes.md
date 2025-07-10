# 🔠 Strings in Python

## ✅ What is a String?
- A **string** is a sequence of characters enclosed in single `' '`, double `" "`, or triple quotes `''' '''` / `""" """`.
- Strings are **immutable** (you can’t change characters directly).
name = "Divya"

## String Indexing & Slicing
text = "Hello Python"

# Indexing
print(text[0])   # H
print(text[-1])  # n

# Slicing
print(text[0:5])     # Hello
print(text[:5])      # Hello
print(text[6:])      # Python
print(text[::-1])    # Reverse string

## Useful String Methods
| Method              | Description                                 |
| ------------------- | ------------------------------------------- |
| `lower()`           | Converts to lowercase                       |
| `upper()`           | Converts to uppercase                       |
| `capitalize()`      | Capitalizes first letter                    |
| `title()`           | Capitalizes first letter of every word      |
| `strip()`           | Removes leading/trailing spaces             |
| `replace(old, new)` | Replaces substring                          |
| `find(sub)`         | Returns first index of sub, -1 if not found |
| `count(sub)`        | Counts occurrences of substring             |
| `split()`           | Splits string into list                     |
| `join(iterable)`    | Joins iterable with string separator        |

## Looping Through Strings
for char in "Python":
    print(char)

## String Formatting
name = "Divya"
age = 20

# f-string (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# format() method
print("My name is {} and I am {} years old.".format(name, age))

## Immutability
text = "hello"
# text[0] = 'H'  Not allowed (TypeError)

## Membership & Comparison
"Py" in "Python"        # True
"java" not in "Python"  # True

"apple" == "Apple"      # False (case-sensitive)

## Use Cases
Data parsing

Input validation

Searching and cleaning text

Building output dynamically

## Python Dictionaries – Quick Notes
🔹 What is a Dictionary?
A dictionary is a collection of key-value pairs.

It is unordered, mutable, and indexed.

Keys must be unique and immutable (e.g., strings, numbers, tuples).

my_dict = {
  "name": "Divya",
  "age": 20,
  "college": "MITS"
}

## Accessing Values
print(my_dict["name"])        # Output: Divya
print(my_dict.get("age"))     # Output: 20

## Adding or Updating Values
my_dict["branch"] = "CSE"     # Add new key
my_dict["age"] = 21           # Update value

## Removing Items
my_dict.pop("age")            # Remove by key
del my_dict["college"]        # Remove using del
my_dict.clear()               # Remove all

## Looping Through a Dictionary
for key in my_dict:
    print(key, ":", my_dict[key])

for key, value in my_dict.items():
    print(key, value)

##  Dictionary Methods
| Method     | Description                        |
| ---------- | ---------------------------------- |
| `get()`    | Returns value for key              |
| `keys()`   | Returns list of keys               |
| `values()` | Returns list of values             |
| `items()`  | Returns list of (key, value) pairs |
| `update()` | Updates dictionary with another    |
| `pop()`    | Removes key and returns value      |
| `clear()`  | Empties the dictionary             |

## Dictionary Comprehension
squares = {x: x*x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 🔸 Sets in Python

## ✅ What is a Set?
- A **set** is an **unordered**, **unindexed** collection of **unique elements**.
- Sets are **mutable**, but the elements must be **immutable**.
- Sets automatically remove duplicates.
example = {1, 2, 3, 4}

## Key Characteristics:
No duplicates allowed.

No indexing or slicing (unordered).

Elements can’t be lists or other sets (but can be tuples).

## Creating a Set
# Using curly braces
my_set = {1, 2, 3}

# Using the set() constructor
empty_set = set()
string_set = set("hello")  # {'h', 'e', 'l', 'o'}

## Common Methods
| Method          | Description                                |
| --------------- | ------------------------------------------ |
| `add(elem)`     | Adds a single element                      |
| `update(iter)`  | Adds multiple elements                     |
| `remove(elem)`  | Removes element; raises error if not found |
| `discard(elem)` | Removes element; does **not** raise error  |
| `pop()`         | Removes and returns a random element       |
| `clear()`       | Removes all elements                       |


## Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)             # {1, 2, 3, 4, 5}
a.intersection(b)      # {3}
a.difference(b)        # {1, 2}
a.symmetric_difference(b)  # {1, 2, 4, 5}

a | b     # Union
a & b     # Intersection
a - b     # Difference
a ^ b     # Symmetric Difference

## Membership Testing
3 in a        # True
10 not in a   # True

## Use Cases of Sets
Removing duplicates from lists.

Fast membership testing (in).

Set operations in logic or data comparison.

## Notes
set() with no arguments creates an empty set.

{} creates an empty dictionary — not a set.

Sets are not subscriptable — you can’t access by index.

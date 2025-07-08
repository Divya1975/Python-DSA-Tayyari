# 📘 Python Tuples - Notes

## ✅ What is a Tuple?
A tuple is a collection which is **ordered** and **immutable**.
- Defined using **parentheses `()`**.
- Items cannot be changed after creation.

my_tuple = (1, 2, 3)

## Tuple vs List
| Feature     | Tuple       | List              |
| ----------- | ----------- | ----------------- |
| Syntax      | `(1, 2, 3)` | `[1, 2, 3]`       |
| Mutability  | ❌ Immutable | ✅ Mutable         |
| Performance | ✅ Faster    | ❌ Slightly Slower |
| Use Case    | Fixed data  | Dynamic data      |

## Accessing Tuple Elements
t = (10, 20, 30)
print(t[1])        # 20
print(t[-1])       # 30

## Tuple Methods
t = (1, 2, 2, 3)

print(t.count(2))   # 2
print(t.index(3))   # 3

## Tuple Packing & Unpacking
# Packing
info = ("Divya", 21, "India")

# Unpacking
name, age, country = info
print(name, age, country)

## When to Use Tuples?
When you want to make sure data cannot be modified.

For returning multiple values from a function.

As keys in a dictionary (because tuples are hashable).


## Tuple with Single Element
t = (5,)       # Note the comma!
print(type(t)) # <class 'tuple'>

## Summary
Tuples are fixed-size collections.

Use () and commas.

Very useful for data integrity and performance.

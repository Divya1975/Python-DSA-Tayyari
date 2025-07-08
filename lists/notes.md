# 📋 Python Lists – Notes

## 🔹 What is a List?
A **list** is a collection of items in a particular order.  
Lists are **mutable** (can be changed), and they can store different data types.


fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4, 5]

## List Creation
empty_list = []
mixed_list = [1, "hello", 3.14, True]

## List Indexing
Indexing starts from 0

my_list = [10, 20, 30]
print(my_list[0])  # Output: 10
print(my_list[-1]) # Output: 30 (last element)

## Looping Through a List
for item in my_list:
    print(item)
    
## Common List Methods
| Method         | Description                             |
| -------------- | --------------------------------------- |
| `append(x)`    | Add item `x` at the end                 |
| `insert(i, x)` | Insert item `x` at index `i`            |
| `remove(x)`    | Remove first occurrence of `x`          |
| `pop()`        | Remove and return last item             |
| `pop(i)`       | Remove and return item at index `i`     |
| `sort()`       | Sort the list in ascending order        |
| `reverse()`    | Reverse the list                        |
| `clear()`      | Remove all items                        |
| `index(x)`     | Return index of first occurrence of `x` |
| `count(x)`     | Count how many times `x` appears        |


## List Operations
a = [1, 2, 3]
b = [4, 5]
print(a + b)      # Concatenation
print(a * 2)      # Repeat list

##  List Slicing
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])   # [1, 2, 3]
print(nums[:3])    # [0, 1, 2]
print(nums[::2])   # [0, 2, 4]

## List Comprehension
A concise way to create lists.
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

## Copying Lists (Avoid Errors!)
original = [1, 2, 3]
copy = original[:]  # or use list(original)

## Nested Lists
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # Output: 3

## Lists are one of the most important and versatile data structures in Python. Mastering their methods and tricks will help in all kinds of coding problems.

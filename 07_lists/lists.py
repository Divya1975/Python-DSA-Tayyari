# ✅ Creating Lists
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
mixed = [1, "hello", 3.14, True]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# 🔢 Accessing Elements
print("\nFirst fruit:", fruits[0])
print("Last number:", numbers[-1])

# 🔁 Looping Through a List
print("\nAll fruits:")
for fruit in fruits:
    print(fruit)

# 🧱 Adding Elements
fruits.append("orange")
numbers.insert(2, 25)
print("\nAfter append and insert:", fruits, numbers)

# ❌ Removing Elements
fruits.remove("banana")         # remove by value
last_num = numbers.pop()        # remove last item
second_num = numbers.pop(1)     # remove by index
print("\nAfter remove & pop:", fruits, numbers)

# 🔄 Changing Elements
fruits[0] = "kiwi"
print("\nUpdated fruits:", fruits)

# 🧹 Clearing a List
temp = [1, 2, 3]
temp.clear()
print("\nCleared list:", temp)

# 📊 List Methods
print("\nCount of 'apple':", fruits.count("apple"))
print("Index of mango:", fruits.index("mango"))

# 🪄 Sorting and Reversing
numbers = [5, 3, 9, 1]
numbers.sort()
print("\nSorted numbers:", numbers)
numbers.reverse()
print("Reversed numbers:", numbers)

# 📐 List Slicing
sliced = numbers[1:3]
print("\nSliced list:", sliced)

# 🎯 List Comprehension
squares = [x**2 for x in range(1, 6)]
print("\nSquares from 1 to 5:", squares)

# 🔂 Nested Lists
matrix = [[1, 2], [3, 4]]
print("\nNested List Element:", matrix[1][0])  # Output: 3

# sets.py

# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}  # duplicates are removed
print("Set of fruits:", fruits)

# Using set() constructor
numbers = set([1, 2, 3, 4, 2, 1])
print("Set of numbers:", numbers)

# Adding elements
fruits.add("orange")
print("After adding orange:", fruits)

# Adding multiple elements
fruits.update(["grape", "mango"])
print("After adding grape and mango:", fruits)

# Removing elements
fruits.remove("banana")  # will raise error if not found
print("After removing banana:", fruits)

fruits.discard("pineapple")  # won't raise error if not found
print("After discarding pineapple:", fruits)

# Pop element (random)
removed_item = fruits.pop()
print("Randomly removed item:", removed_item)
print("Set after pop:", fruits)

# Clear the set
temp_set = {"one", "two", "three"}
temp_set.clear()
print("After clearing:", temp_set)

# Set Operations
A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A.union(B))                # or A | B
print("Intersection:", A.intersection(B))  # or A & B
print("Difference (A - B):", A.difference(B))  # or A - B
print("Symmetric Difference:", A.symmetric_difference(B))  # or A ^ B

# Membership Test
print("Is 2 in A?", 2 in A)
print("Is 10 not in A?", 10 not in A)

# Set from string
char_set = set("balloon")
print("Unique characters in 'balloon':", char_set)

# Creating a tuple
fruits = ("apple", "banana", "cherry")
print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing tuples
print("First two fruits:", fruits[:2])

# Length of tuple
print("Total fruits:", len(fruits))

# Tuple with mixed data types
person = ("Divya", 21, "India")
print("Mixed tuple:", person)

# Tuple unpacking
name, age, country = person
print("Name:", name)
print("Age:", age)
print("Country:", country)

# Tuple with single element (IMPORTANT!)
single = ("hello",)
print("Single element tuple:", single)
print("Type:", type(single))  # <class 'tuple'>

# Nested tuple
nested = (1, 2, (3, 4))
print("Nested tuple:", nested)
print("Access nested element:", nested[2][0])

# Using count() and index()
nums = (1, 2, 2, 3, 4, 2)
print("Count of 2:", nums.count(2))   # 3
print("Index of 3:", nums.index(3))   # 3

# Looping through a tuple
for fruit in fruits:
    print("Fruit:", fruit)

# Trying to modify (This will raise an error)
# fruits[0] = "mango"  #  Tuples are immutable

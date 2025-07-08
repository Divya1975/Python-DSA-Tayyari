# 1. Create a tuple of your 5 favorite colors and print each using a loop
colors = ("pink", "purple", "blue", "peach", "white")
print("Favorite Colors:")
for color in colors:
    print("-", color)

# 2. Create a tuple of 3 numbers and calculate their average
numbers = (10, 20, 30)
average = sum(numbers) / len(numbers)
print("Average:", average)

# 3. Unpack a tuple of your profile data and print them
profile = ("Divya", 21, "India")
name, age, country = profile
print("Name:", name)
print("Age:", age)
print("Country:", country)

# 4. Create a tuple and count how many times a value appears
marks = (85, 90, 75, 90, 95, 90)
print("90 appears", marks.count(90), "times")

# 5. Try to change a value in a tuple (this should give an error)
try:
    marks[0] = 100
except TypeError as e:
    print("Error:", e)

# 6. Create a tuple with one element and check its type
single = ("only_one",)
print("Single element tuple:", single)
print("Type:", type(single))

# 7. Check if an item exists in a tuple
if "purple" in colors:
    print("Yes, purple is a favorite color!")

# 8. Combine two tuples and print the result
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined = tuple1 + tuple2
print("Combined tuple:", combined)

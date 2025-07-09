# 1. Creating a dictionary
student = {
    "name": "Divya",
    "age": 20,
    "branch": "CSE",
    "college": "MITS Gwalior"
}
print("Student Dictionary:", student)

# 2. Accessing values
print("Name:", student["name"])
print("Branch:", student.get("branch"))

# 3. Adding a new key-value pair
student["year"] = "2nd Year"
print("Updated Dictionary:", student)

# 4. Updating a value
student["age"] = 21
print("After Updating Age:", student)

# 5. Removing a key
student.pop("college")
print("After Removing 'college':", student)

# 6. Looping through dictionary
print("\nAll Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# 7. Using dictionary methods
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 8. Nested Dictionary
course = {
    "python": {
        "duration": "3 months",
        "level": "beginner"
    },
    "java": {
        "duration": "4 months",
        "level": "intermediate"
    }
}
print("\nNested Dictionary:", course)
print("Python Course Duration:", course["python"]["duration"])

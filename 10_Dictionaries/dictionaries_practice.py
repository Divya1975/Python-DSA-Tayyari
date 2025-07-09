# Q1. Count the frequency of each character in a string
text = "dictionary practice is fun"
freq = {}
for char in text:
    if char != " ":
        freq[char] = freq.get(char, 0) + 1
print("Character Frequency:\n", freq)

# Q2. Create a dictionary from two lists
keys = ["name", "age", "branch"]
values = ["Divya", 20, "CSE"]
student = dict(zip(keys, values))
print("\nStudent Dictionary:", student)

# Q3. Find the key with the maximum value
scores = {"math": 88, "science": 92, "english": 85}
max_subject = max(scores, key=scores.get)
print("\nTop Scoring Subject:", max_subject)

# Q4. Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print("\nMerged Dictionary:", merged)

# Q5. Reverse keys and values
original = {"apple": "red", "banana": "yellow", "grape": "purple"}
reversed_dict = {value: key for key, value in original.items()}
print("\nReversed Dictionary:", reversed_dict)

# Q6. Group students by branch
students = [
    {"name": "Divya", "branch": "CSE"},
    {"name": "Riya", "branch": "IT"},
    {"name": "Anu", "branch": "CSE"},
    {"name": "Kriti", "branch": "IT"}
]

grouped = {}
for student in students:
    branch = student["branch"]
    grouped.setdefault(branch, []).append(student["name"])

print("\nGrouped by Branch:", grouped)

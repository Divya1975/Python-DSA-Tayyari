# strings.py

# 1. Creating strings
str1 = "Hello"
str2 = 'Python'
str3 = """This is
a multi-line
string"""
print(str1)
print(str2)
print(str3)

# 2. String indexing and slicing
message = "LearningPython"
print("First character:", message[0])
print("Last character:", message[-1])
print("Substring (0 to 8):", message[0:8])
print("Reversed string:", message[::-1])

# 3. String methods
sample = "  hello world  "

print("\nOriginal:", sample)
print("Lowercase:", sample.lower())
print("Uppercase:", sample.upper())
print("Title Case:", sample.title())
print("Capitalize:", sample.capitalize())
print("Stripped:", sample.strip())
print("Replaced:", sample.replace("hello", "hi"))
print("Count of 'l':", sample.count('l'))
print("Index of 'world':", sample.find("world"))

# 4. Splitting and Joining
words = sample.strip().split()
print("Split:", words)

joined = "-".join(words)
print("Joined with hyphen:", joined)

# 5. String formatting
name = "Divya"
age = 20
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

# 6. Looping through a string
print("\nCharacters in 'Python':")
for ch in "Python":
    print(ch)

# 7. Membership test
print("Is 'Py' in 'Python'? :", "Py" in "Python")
print("Is 'java' not in 'Python'? :", "java" not in "Python")

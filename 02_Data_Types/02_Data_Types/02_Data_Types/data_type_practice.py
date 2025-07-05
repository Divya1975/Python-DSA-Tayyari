# PQ1: Type Identification
a = 5
b = 5.0
c = "5"
d = 5 + 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# PQ2: Data Type Conversion
x = "10"
y = 3
z = int(x) + y
print(z)

# PQ3: Mutable vs Immutable
a = [1, 2, 3]
b = a
b.append(4)
print("List a:", a)

# PQ4: Set Uniqueness
items = {1, 2, 2, 3, 3, 3}
print(items)

# PQ5: Dictionary + Boolean
person = {
    "name": "Divya",
    "age": 20,
    "is_student": True
}
print(person["name"])
print(type(person["is_student"]))

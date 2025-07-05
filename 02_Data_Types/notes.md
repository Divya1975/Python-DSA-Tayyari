# Python Data Types

In Python, everything is an object. Each value has a data type.

---

### 🔹 Built-in Data Types:

1. **Numeric Types**:
   - `int`: Integer → x = 5
   - `float`: Decimal → y = 3.14
   - `complex`: Complex → z = 3 + 4j

2. **Text Type**:
   - `str`: String → name = "Divya"

3. **Sequence Types**:
   - `list`: Mutable → l = [1, 2, 3]
   - `tuple`: Immutable → t = (1, 2, 3)
   - `range`: Sequence → range(5)

4. **Set Types**:
   - `set`: Unordered, unique → s = {1, 2, 3}

5. **Mapping Type**:
   - `dict`: Key-value → d = {"name": "Divya"}

6. **Boolean Type**:
   - `bool`: True / False → flag = True

7. **Binary Types**:
   - `bytes`, `bytearray`, `memoryview`

---

### 🔸 Type Checking:
```python
type(5)   # <class 'int'>
int("10"), float("4.5"), str(123)

✅ **Commit new file** after pasting

---

## 🔹 Step 2: Code File Banao (`data_types.py`)

### 📄 Filename:

### 💻 Paste this code:

```python
# Numeric Types
x = 10
y = 3.14
z = 3 + 2j

print("Integer:", x)
print("Float:", y)
print("Complex:", z)

# String
name = "Divya"
print("String:", name)

# List
numbers = [1, 2, 3, 4]
print("List:", numbers)

# Tuple
coordinates = (10, 20)
print("Tuple:", coordinates)

# Set
unique = {1, 2, 2, 3}
print("Set (Unique):", unique)

# Dictionary
student = {"name": "Divya", "age": 20}
print("Dictionary:", student)

# Boolean
is_valid = True
print("Boolean:", is_valid)

# Type Casting
a = int("5")
b = float("4.5")
c = str(100)
print("After casting:", a, b, c)

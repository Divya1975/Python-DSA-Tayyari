#  Hashing – Concept Implementation in Python

#  Using Python Dictionary (Hash Map)
my_hash_map = {}

# Insert
my_hash_map["name"] = "Divya"
my_hash_map["age"] = 21

# Retrieve
print("Name:", my_hash_map["name"])
print("Age:", my_hash_map["age"])

# Check key existence
if "age" in my_hash_map:
    print("Age exists")

# Delete
del my_hash_map["age"]

print("Hash Map after deletion:", my_hash_map)


#  Custom Hash Function (for understanding only)
class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]

    def display(self):
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")


# Demo
print("\n--- Simple Hash Table ---")
ht = SimpleHashTable(10)
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("grape", 300)

print("Value for 'banana':", ht.get("banana"))
ht.display()

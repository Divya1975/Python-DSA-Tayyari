#  Hashing – Notes

Hashing is a technique used to uniquely identify a specific object from a group of similar objects. It is widely used in data structures for fast data access.

---

##  What is Hashing?
- Hashing is a process of mapping data to a fixed-size value called a hash code using a **hash function**.
- The hash code is then used to index into a **hash table** to store or retrieve data efficiently.

---

##  Components of Hashing

1. **Hash Function** – Converts input (key) into a hash code (usually an integer).
   - Example: `hash(key) % table_size`
   - Good hash functions uniformly distribute keys.

2. **Hash Table** – Array where data is stored based on hash code.

---

##  Common Collision Resolution Techniques

- **Chaining**: Store multiple elements at the same index using a list (linked list).
- **Open Addressing**:
  - **Linear Probing**: Next slot is checked linearly.
  - **Quadratic Probing**: Next slot is checked using a quadratic function.
  - **Double Hashing**: Uses a second hash function to find next slot.

---

##  Applications of Hashing

- Data indexing (e.g., hash maps/dictionaries)
- Password storage (hashed passwords)
- Caches (e.g., LRU Cache)
- Sets (removal of duplicates)
- Detecting duplicates in O(1) time on average

---

## ⚙️ Python Dictionary as Hash Table


# Example of hash map in Python
hash_map = {}
hash_map["apple"] = 1
hash_map["banana"] = 2
print(hash_map["banana"])  # Output: 2

---

##  Tips for Interview

- Know basic implementation of hash tables
- Be able to handle collisions
- Practice LeetCode problems like:
  - Two Sum
  - Group Anagrams
  - Longest Consecutive Sequence

---

##  Time Complexity

| Operation     | Average Case | Worst Case (with bad hash or collisions) |
|---------------|--------------|------------------------------------------|
| Insert        | O(1)         | O(n)                                     |
| Search        | O(1)         | O(n)                                     |
| Delete        | O(1)         | O(n)                                     |

---

 **Hashing helps you think beyond arrays. It’s magic for fast lookups!**

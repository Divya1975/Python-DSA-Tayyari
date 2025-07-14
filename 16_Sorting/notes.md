#  Sorting in Python

Sorting means arranging data in a specific order — usually ascending or descending.

---

## Why Sorting is Important?

- Makes searching faster (especially Binary Search)
- Helps in organizing data
- Used in algorithms like merge, quick, and binary search trees

---

##  Types of Sorting Algorithms

---

###  Bubble Sort

- Compares adjacent elements and swaps if needed
- Repeats this until the list is sorted

**Time Complexity:**
- Best: O(n)
- Worst: O(n²)

---

###  Selection Sort

- Finds the minimum element and places it at the beginning
- Repeats this for every position

**Time Complexity:**
- Always O(n²)

---

###  Insertion Sort

- Builds the sorted array one item at a time
- Good for small or nearly sorted datasets

**Time Complexity:**
- Best: O(n)
- Worst: O(n²)

---

###  Merge Sort

- Divide and conquer technique
- Recursively divides the array, sorts, and merges

**Time Complexity:**
- Always O(n log n)

---

###  Quick Sort

- Picks a pivot and partitions the array
- Recursively sorts sub-arrays

**Time Complexity:**
- Best: O(n log n)
- Worst: O(n²) (if pivot is poorly chosen)

---

##  Comparison Table

| Algorithm      | Best    | Worst    | Stable | Space |
|----------------|---------|----------|--------|--------|
| Bubble Sort    | O(n)    | O(n²)    | ✅     | O(1)   |
| Selection Sort | O(n²)   | O(n²)    | ❌     | O(1)   |
| Insertion Sort | O(n)    | O(n²)    | ✅     | O(1)   |
| Merge Sort     | O(n log n) | O(n log n) | ✅ | O(n)   |
| Quick Sort     | O(n log n) | O(n²)  | ❌     | O(log n)

---

## Tip:
Use Python’s built-in `sorted()` or `.sort()` for real-life use cases — they're based on **Timsort** (hybrid of merge + insertion).

---

##  Coming up in code:
- Implementations of Bubble, Selection, Insertion
- Merge & Quick Sort basics

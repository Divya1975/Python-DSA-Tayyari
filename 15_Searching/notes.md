#  Searching in Python

Searching is the process of finding the **position of a desired element** in a data structure like a list or array.

There are mainly two types of searching techniques:

---

##  Linear Search

### Description:
- It checks every element one by one.
- Useful for **unsorted** lists.

### Time Complexity:
- **Best Case**: O(1)
- **Worst Case**: O(n)

### How it Works:
- Start from index 0 and go till end.
- Compare each element with the target.

---

##  Binary Search

### Description:
- Works only on **sorted** lists.
- Repeatedly divides the search space in half.

### Time Complexity:
- **Best Case**: O(1)
- **Worst Case**: O(log n)

### 🔧 How it Works:
- Compare middle element with target.
- If equal → return index.
- If target < mid → search in left half.
- If target > mid → search in right half.

---

## When to Use What?

| Type           | Use When            |
|----------------|---------------------|
| Linear Search  | Unsorted data       |
| Binary Search  | Sorted data         |

---

## Real Life Analogy:

- **Linear Search**: Like checking every page in a notebook for a word.
- **Binary Search**: Like checking in a dictionary — jump to the middle, decide to go left/right based on alphabetical order.

---

## More advanced searches:
- Jump Search
- Interpolation Search
- Exponential Search

(We’ll cover them later)

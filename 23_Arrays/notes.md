#  Arrays – Notes

##  What is an Array?
An **array** is a collection of elements stored in contiguous memory locations. All elements are of the same data type and can be accessed using an index.

---

##  Features of Arrays
- Fixed size
- Homogeneous elements
- Random access via index
- Stored in contiguous memory blocks

---

##  Basic Operations
- **Traverse**: Visit all elements
- **Insert**: Add an element (at index, end)
- **Delete**: Remove an element
- **Search**: Find an element (linear/binary)
- **Update**: Change the value at a specific index

---

##  Time Complexities

| Operation   | Time Complexity |
|-------------|------------------|
| Access      | O(1)             |
| Search      | O(n)             |
| Insertion   | O(n) (worst case)|
| Deletion    | O(n)             |

---

##  Use Cases
- Lookup tables
- Sorting algorithms (like QuickSort, MergeSort)
- Matrix representation
- Caching and buffering
- Image processing

---

##  Array vs List in Python
- Python's `list` is a dynamic array
- Python also has arrays using the `array` module (less common)
- `NumPy` provides powerful multi-dimensional arrays (`ndarray`)

---

##  Array Implementation (Python List Example)

arr = [10, 20, 30]
arr.append(40)        # Insert at end
arr.insert(1, 15)     # Insert at index 1
arr.remove(20)        # Delete by value
print(arr[2])         # Access by index

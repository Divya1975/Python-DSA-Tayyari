#  Python Arrays (Lists) - Concepts and Examples

#  Create an array (list in Python)
arr = [10, 20, 30, 40, 50]

#  Access elements
print("First Element:", arr[0])       # Output: 10
print("Last Element:", arr[-1])       # Output: 50

#  Modify elements
arr[1] = 25
print("Modified Array:", arr)         # Output: [10, 25, 30, 40, 50]

#  Add elements
arr.append(60)                        # Add to end
arr.insert(2, 99)                     # Insert at index 2
print("After Insertions:", arr)

#  Remove elements
arr.remove(30)                        # Remove first occurrence of 30
popped = arr.pop()                   # Remove last element
print("After Deletions:", arr)
print("Popped Element:", popped)

#  Search for an element
if 40 in arr:
    print("40 is present at index", arr.index(40))

#  Loop through an array
for i, val in enumerate(arr):
    print(f"Index {i}: Value {val}")

#  Sort and Reverse
arr.sort()
print("Sorted Array:", arr)
arr.reverse()
print("Reversed Array:", arr)

#  Length of array
print("Length of Array:", len(arr))

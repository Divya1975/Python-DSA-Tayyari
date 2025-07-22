#  Practice Problems on Arrays (Python Lists)

#  Sum of all elements
arr = [5, 10, 15, 20]
total = sum(arr)
print("Total Sum:", total)  # Output: 50

#  Find maximum and minimum
print("Max:", max(arr))     # Output: 20
print("Min:", min(arr))     # Output: 5

#  Count occurrences of an element
nums = [1, 2, 2, 3, 4, 2, 5]
print("Count of 2:", nums.count(2))  # Output: 3

#  Remove duplicates from array
unique = list(set(nums))
print("Unique Elements:", unique)

#  Find second largest element
arr = [10, 25, 30, 45, 30]
unique_sorted = sorted(set(arr), reverse=True)
if len(unique_sorted) >= 2:
    print("Second Largest:", unique_sorted[1])  # Output: 30

#  Reverse an array without using reverse()
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]
print("Reversed:", reversed_arr)

#  Merge two arrays
a = [1, 3, 5]
b = [2, 4, 6]
merged = a + b
print("Merged Array:", merged)

#  Check if array is sorted
def is_sorted(arr):
    return arr == sorted(arr)

print("Is Sorted?", is_sorted([1, 2, 3]))   # True
print("Is Sorted?", is_sorted([3, 2, 1]))   # False

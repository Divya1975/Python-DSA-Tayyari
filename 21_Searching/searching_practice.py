#  PRACTICE PROBLEMS FOR SEARCHING 

# Q1: Check if a number exists in a list using Linear Search

def is_present_linear(arr, target):
    return linear_search(arr, target) != -1

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Q2: Find the position of an element using Binary Search (Iterative)

def find_position_binary(arr, target):
    arr.sort()  # Binary Search requires sorted array
    return binary_search_iterative(arr, target)

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Q3: Return True if element exists using Binary Search (Recursive)

def exists_recursive_binary(arr, target):
    arr.sort()
    index = binary_search_recursive(arr, target, 0, len(arr)-1)
    return index != -1

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


#  Sample Test
if __name__ == "__main__":
    data = [10, 4, 2, 8, 6, 7]

    print("Q1:", is_present_linear(data, 8))  # True
    print("Q2:", find_position_binary(data, 6))  # Index (after sorting)
    print("Q3:", exists_recursive_binary(data, 5))  # False

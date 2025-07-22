#  Linear Search Implementation

def linear_search(arr, target):
    """
    Searches for the target value using linear search.

    Args:
        arr (list): The list of elements
        target (any): The value to search for

    Returns:
        int: Index of target if found, else -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


#  Binary Search Implementation (Iterative)

def binary_search_iterative(arr, target):
    """
    Searches for the target value using iterative binary search.

    Args:
        arr (list): Sorted list of elements
        target (any): The value to search for

    Returns:
        int: Index of target if found, else -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


#  Binary Search Implementation (Recursive)

def binary_search_recursive(arr, target, left, right):
    """
    Searches for the target value using recursive binary search.

    Args:
        arr (list): Sorted list of elements
        target (any): The value to search for
        left (int): Left index
        right (int): Right index

    Returns:
        int: Index of target if found, else -1
    """
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

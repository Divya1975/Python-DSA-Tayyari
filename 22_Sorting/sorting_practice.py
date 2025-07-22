#  PRACTICE QUESTIONS FOR SORTING ALGORITHMS

from sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

# Q1: Sort a list using Bubble Sort
def sort_with_bubble(arr):
    return bubble_sort(arr.copy())


# Q2: Sort a list using Selection Sort
def sort_with_selection(arr):
    return selection_sort(arr.copy())


# Q3: Sort a list using Insertion Sort
def sort_with_insertion(arr):
    return insertion_sort(arr.copy())


# Q4: Sort a list using Merge Sort
def sort_with_merge(arr):
    return merge_sort(arr.copy())


# Q5: Sort a list using Quick Sort
def sort_with_quick(arr):
    return quick_sort(arr.copy())


#  Test All Sorting Methods
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original:", data)

    print("\n Bubble Sort:", sort_with_bubble(data))
    print("Selection Sort:", sort_with_selection(data))
    print("Insertion Sort:", sort_with_insertion(data))
    print("Merge Sort:", sort_with_merge(data))
    print("Quick Sort:", sort_with_quick(data))

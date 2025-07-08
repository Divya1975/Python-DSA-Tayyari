# Q1️⃣: Find the maximum number in a list
def find_max(lst):
    return max(lst)

print("Max number:", find_max([3, 7, 2, 9, 4]))


# Q2️⃣: Count how many times an element appears
def count_occurrences(lst, element):
    return lst.count(element)

print("Occurrences of 3:", count_occurrences([1, 3, 3, 4, 3], 3))


# Q3️⃣: Remove all even numbers from a list
def remove_evens(lst):
    return [x for x in lst if x % 2 != 0]

print("Without evens:", remove_evens([1, 2, 3, 4, 5, 6]))


# Q4️⃣: Reverse a list without using reverse()
def reverse_list(lst):
    return lst[::-1]

print("Reversed list:", reverse_list([1, 2, 3, 4]))


# Q5️⃣: Merge two lists and sort them
def merge_and_sort(list1, list2):
    return sorted(list1 + list2)

print("Merged and sorted:", merge_and_sort([3, 1, 5], [6, 2, 4]))

#  Hashing Practice Problems in Python

#  Q1. Count frequency of elements in a list using hashing
def count_frequencies(arr):
    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map

arr = [1, 2, 2, 3, 3, 3, 4]
print("Frequencies:", count_frequencies(arr))


#  Q2. Find the first non-repeating element in a list
def first_non_repeating(arr):
    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1
    for item in arr:
        if freq_map[item] == 1:
            return item
    return None

arr2 = [4, 5, 1, 2, 0, 4]
print("First non-repeating:", first_non_repeating(arr2))


#  Q3. Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print("Anagram check (listen/silent):", are_anagrams("listen", "silent"))
print("Anagram check (hello/world):", are_anagrams("hello", "world"))


#  Q4. Find duplicates in an array using hashing
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

arr3 = [1, 2, 3, 1, 2, 4]
print("Duplicates:", find_duplicates(arr3))

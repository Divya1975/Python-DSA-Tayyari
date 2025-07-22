# recursion_advanced_practice.py

#  Q1: Sum of Digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
print("Sum of digits of 1234:", sum_of_digits(1234))  # Output: 10

#  Q2: Count Zeros in a Number
def count_zeros(n):
    if n == 0:
        return 1
    if n < 10:
        return 1 if n == 0 else 0
    return (1 if n % 10 == 0 else 0) + count_zeros(n // 10)
print("Number of zeros in 102030:", count_zeros(102030))  # Output: 3

#  Q3: Product of Digits
def product_of_digits(n):
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)
print("Product of digits of 1234:", product_of_digits(1234))  # Output: 24

#  Q4: Palindrome Check Using Recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print("Is 'madam' a palindrome?:", is_palindrome("madam"))  # Output: True
print("Is 'hello' a palindrome?:", is_palindrome("hello"))  # Output: False

#  Q5: Reverse a String Recursively
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]
print("Reverse of 'recursion':", reverse_string("recursion"))  # Output: noisrucer

#  Q6: Recursive Binary Search
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
arr = [1, 3, 5, 7, 9, 11]
print("Index of 7:", binary_search(arr, 7, 0, len(arr) - 1))  # Output: 3

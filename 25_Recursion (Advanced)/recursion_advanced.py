# recursion_advanced.py

#  Head Recursion Example
def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print(n, end=" ")
print("Head Recursion:")
head_recursion(5)  # Output: 1 2 3 4 5

#  Tail Recursion Example
def tail_recursion(n):
    if n == 0:
        return
    print(n, end=" ")
    tail_recursion(n - 1)
print("\nTail Recursion:")
tail_recursion(5)  # Output: 5 4 3 2 1

#  Factorial Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("\nFactorial of 5:", factorial(5))  # Output: 120

#  Fibonacci Using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci(6):", fibonacci(6))  # Output: 8

#  Backtracking: Generate all subsets
def subsets(arr, index=0, current=[]):
    if index == len(arr):
        print(current)
        return
    # Include the element
    subsets(arr, index + 1, current + [arr[index]])
    # Exclude the element
    subsets(arr, index + 1, current)
print("All subsets of [1, 2]:")
subsets([1, 2])

#  Backtracking: Permutations
def permutations(s, chosen=""):
    if len(s) == 0:
        print(chosen)
        return
    for i in range(len(s)):
        c = s[i]
        remaining = s[:i] + s[i+1:]
        permutations(remaining, chosen + c)
print("Permutations of 'abc':")
permutations("abc")

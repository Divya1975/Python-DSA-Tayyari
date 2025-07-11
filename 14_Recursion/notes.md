## What is Recursion?
Recursion is a method of solving a problem where a function calls itself to solve smaller instances of the same problem.

## Syntax of a Recursive Function

def function_name(parameters):
    if base_condition:
        return result
    else:
        return function_name(smaller_problem)

## Key Concepts
Base Case: The condition under which the function stops calling itself.

Recursive Case: The part where the function calls itself with modified input.

## Example 1: Factorial Using Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

## Example 2: Fibonacci Series
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8

## Example 3: Sum of Natural Numbers
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

print(sum_natural(5))  # Output: 15

## Recursion vs Iteration

| Feature      | Recursion             | Iteration               |
| ------------ | --------------------- | ----------------------- |
| Structure    | Function calls itself | Loops (for, while)      |
| Memory Usage | More (call stack)     | Less                    |
| Speed        | Can be slower         | Usually faster          |
| Readability  | Often more elegant    | Sometimes more readable |

## When to Use Recursion?
Problems that can be broken down into smaller, similar subproblems.

Tree traversals, factorials, Fibonacci, backtracking, divide and conquer algorithms (like merge sort, quick sort).

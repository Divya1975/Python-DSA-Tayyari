#  Recursion (Advanced)

Recursion is a method of solving problems where the solution depends on solving smaller instances of the same problem.

---

##  Tail Recursion vs Head Recursion

- **Head Recursion**: Recursive call happens before any operation.

def head(n):
    if n == 0:
        return
    head(n - 1)
    print(n)


- **Tail Recursion**: Recursive call is the last statement in the function.

def tail(n):
    if n == 0:
        return
    print(n)
    tail(n - 1)


---

##  Backtracking

- Technique for solving problems recursively by trying to build a solution incrementally.
- Used in puzzles, permutations, combinations, etc.

Example: N-Queens, Sudoku Solver

---

##  Recursion Tree & Space Complexity

- Each recursive call adds a new frame to the stack.
- Space complexity = depth of recursion × space per call.

---

##  Use Cases of Recursion

- Tree traversals (Inorder, Preorder, Postorder)
- Graph traversals (DFS)
- Divide and conquer algorithms (Merge Sort, Quick Sort)
- Dynamic Programming (Top-down)
- Generating subsets, permutations, combinations

---

##  Tips

- Always define base case.
- Think of how to reduce the problem.
- Watch out for stack overflow!
- Use memoization if overlapping subproblems exist.

---

##  Summary

| Concept           | Description                               |
|------------------|-------------------------------------------|
| Base Case         | Stops recursion                           |
| Recursive Case    | Calls itself with smaller input           |
| Stack Overflow    | When recursion goes too deep              |
| Memoization       | Store results to avoid recomputation      |
| Backtracking      | Try all options, undo if not valid        |

---


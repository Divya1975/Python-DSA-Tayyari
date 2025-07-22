#  Stack & Queue – Notes

---

##  What is a Stack?

- **LIFO** – Last In, First Out
- Think of a stack of plates: you can only take the top one off.
- Common operations:
  - `push()` → add element to the top
  - `pop()` → remove top element
  - `peek()` → view top element
  - `isEmpty()` → check if stack is empty

###  Python Implementation
- Using list (with append and pop)
- Using `collections.deque` for better performance

---

##  What is a Queue?

- **FIFO** – First In, First Out
- Think of people standing in a line: first one gets served first.
- Common operations:
  - `enqueue()` → add element to the end
  - `dequeue()` → remove from front
  - `peek()` → view front element
  - `isEmpty()` → check if queue is empty

###  Python Implementation
- Using `collections.deque`
- Queue module (less common for DSA)

---

##  When to Use

| Scenario                                | Stack or Queue |
|-----------------------------------------|----------------|
| Undo feature in editor                  | Stack          |
| Function call stack                     | Stack          |
| Printer job scheduling                  | Queue          |
| BFS (Breadth First Search) traversal    | Queue          |
| Balancing symbols/brackets              | Stack          |
| Customer service ticketing system       | Queue          |

---

##  Tip

> Use `deque` from `collections` for both stacks and queues in Python – it's optimized for fast appends and pops from both ends.

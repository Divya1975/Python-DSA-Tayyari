#  29. Heap & Priority Queue

##  What is a Heap?
- A **heap** is a special tree-based data structure that satisfies the **heap property**:
  - **Max-Heap**: Parent is **greater than or equal to** its children
  - **Min-Heap**: Parent is **less than or equal to** its children

- It’s usually implemented as a **binary heap** using an array.

##  Applications of Heap
- Priority Queues
- Dijkstra's shortest path algorithm
- Heap sort
- Top K frequent elements
- Scheduling tasks

---

##  Properties
- Complete Binary Tree (all levels filled except last)
- Operations:
  - `insert()`: O(log n)
  - `extractMin()/extractMax()`: O(log n)
  - `peek()`: O(1)
  - `heapify()`: O(log n)

---

##  Priority Queue
- A **Priority Queue** is an abstract data type where each element has a priority.
- Elements with **higher priority are served before** those with lower priority.

➡️ Usually implemented using **heap**.

---

##  Heap as an Array

For index `i`:
- Left Child → `2*i + 1`
- Right Child → `2*i + 2`
- Parent → `(i - 1) // 2`

---

##  Python `heapq` Module


import heapq

# Min-Heap by default
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)

print(heapq.heappop(min_heap))  # 1

# Max-Heap (by pushing negative values)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)

print(-heapq.heappop(max_heap))  # 5


---

##  Custom Priority Queue with Tuples


tasks = []
heapq.heappush(tasks, (2, "Clean"))
heapq.heappush(tasks, (1, "Code"))
heapq.heappush(tasks, (3, "Sleep"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Task: {task}, Priority: {priority}")


---


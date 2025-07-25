#  Chapter 28: Graphs in Python

Graphs are one of the most powerful data structures for modeling real-world relationships and problems. They are widely used in computer networks, social networks, maps, and many algorithms like search engines and recommendation systems.

---

##  Key Concepts

### ➤ Graph Terminology:
- **Vertex (Node):** Fundamental unit of the graph.
- **Edge:** Connection between two nodes.
- **Adjacent Node:** A node connected directly to another.
- **Degree:** Number of edges connected to a node.

---

##  Graph Representations

### 1. **Adjacency Matrix**
- A 2D array where `matrix[i][j] = 1` if there is an edge from `i` to `j`.
- Suitable for dense graphs.

### 2. **Adjacency List**
- A dictionary where each key is a node, and the value is a list of neighbors.
- Space efficient for sparse graphs.


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['D']
}


---

##  Graph Traversal

###  Depth First Search (DFS)

- Recursive or using a stack.
- Explores as far as possible before backtracking.


def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


###  Breadth First Search (BFS)

- Uses a queue.
- Explores neighbors first before going deeper.


from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])


---

##  Directed vs Undirected Graph

- **Directed:** Edges have direction (A → B).
- **Undirected:** Edges don't have direction (A — B).

---

##  Weighted Graph

- Each edge has a weight or cost (e.g., distance, time).
- Represented using tuples or dictionaries:

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4)],
    'C': [('E', 5)],
    'D': [],
    'E': [('D', 1)]
}


---

##  Applications of Graphs

- Web Crawling
- Social Networks
- Route/Pathfinding Algorithms
- Scheduling Problems
- Network Flows

---

##  Summary

| Concept | Description |
|--------|-------------|
| Representation | Adjacency Matrix, Adjacency List |
| Traversals | DFS (stack/recursion), BFS (queue) |
| Types | Directed, Undirected, Weighted |
| Use Cases | Navigation, social graphs, compilers |

---

 **Quote:**  
_"A graph isn’t just lines and nodes — it’s a map of possibilities."_

---

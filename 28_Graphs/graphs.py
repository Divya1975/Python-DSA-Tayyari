#  Graph Implementation in Python

# Using Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['D']
}

# Depth First Search (DFS)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(f"Visited {node}")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Breadth First Search (BFS)
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(f"Visited {node}")
            visited.add(node)
            queue.extend(graph[node])

# Example Calls
print("DFS Traversal:")
dfs(graph, 'A')

print("\nBFS Traversal:")
bfs(graph, 'A')

#  Weighted Graph Example
weighted_graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4)],
    'C': [('E', 5)],
    'D': [],
    'E': [('D', 1)]
}

# Display weighted edges
print("\nWeighted Graph Edges:")
for node in weighted_graph:
    for neighbor, weight in weighted_graph[node]:
        print(f"{node} -> {neighbor} (weight: {weight})")

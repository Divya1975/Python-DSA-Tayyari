#  Practice: Graph Algorithms in Python

# Directed Graph using Adjacency List
graph = {
    '0': ['1', '2'],
    '1': ['2'],
    '2': ['0', '3'],
    '3': ['3']
}

#  Depth First Search (Recursive)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

#  Breadth First Search (Using Queue)
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(graph[vertex])

print("DFS starting from node 2:")
dfs(graph, '2')
print("\nBFS starting from node 2:")
bfs(graph, '2')

#  Practice: Count number of nodes reachable from a given node
def count_reachable(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    count = 1
    for neighbor in graph[node]:
        if neighbor not in visited:
            count += count_reachable(graph, neighbor, visited)
    return count

print(f"\n\nReachable nodes from node '2': {count_reachable(graph, '2')}")

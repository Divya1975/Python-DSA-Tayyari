import heapq

# --------------------------
#  Min-Heap Example
# --------------------------
min_heap = []

heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 7)

print("🔹 Min-Heap elements (in order):")
while min_heap:
    print(heapq.heappop(min_heap), end=" ")

# Output: 1 5 7 10

print("\n\n")

# --------------------------
#  Max-Heap Example
# --------------------------
max_heap = []

# Insert negative values to simulate max-heap
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -7)

print("🔸 Max-Heap elements (in order):")
while max_heap:
    print(-heapq.heappop(max_heap), end=" ")

# Output: 10 7 5 1

print("\n\n")

# --------------------------
#  Priority Queue with Tuples
# --------------------------
tasks = []
heapq.heappush(tasks, (2, "Do laundry"))
heapq.heappush(tasks, (1, "Finish DSA"))
heapq.heappush(tasks, (3, "Watch movie"))

print("Task Priority Queue:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Task: {task}, Priority: {priority}")

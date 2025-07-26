import heapq

# Practice 1: Implement a function to return k smallest elements from a list
def k_smallest_elements(nums, k):
    return heapq.nsmallest(k, nums)

# Practice 2: Implement a function to return k largest elements from a list
def k_largest_elements(nums, k):
    return heapq.nlargest(k, nums)

# Practice 3: Use heap as a priority queue for custom tasks
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, priority, task_name):
        heapq.heappush(self.tasks, (priority, task_name))

    def complete_task(self):
        if self.tasks:
            priority, task = heapq.heappop(self.tasks)
            return f"Completed Task: {task} (Priority: {priority})"
        return "No tasks available"

# Test code
if __name__ == "__main__":
    print("🔹 K Smallest Elements:", k_smallest_elements([5, 1, 8, 3, 2], 3))
    print("🔸 K Largest Elements:", k_largest_elements([5, 1, 8, 3, 2], 2))

    tm = TaskManager()
    tm.add_task(3, "Write blog")
    tm.add_task(1, "Complete assignment")
    tm.add_task(2, "Practice DSA")

    print(tm.complete_task())
    print(tm.complete_task())
    print(tm.complete_task())

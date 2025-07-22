#  Stack and Queue Implementations in Python

from collections import deque

# -------------------------------
#  STACK IMPLEMENTATION (LIFO)
# -------------------------------

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack (top --> bottom):", self.stack[::-1])


# -------------------------------
#  QUEUE IMPLEMENTATION (FIFO)
# -------------------------------

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue (front --> rear):", list(self.queue))


#  Demo usage (can be removed later)
if __name__ == "__main__":
    print("🔹 STACK DEMO")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print("Popped:", s.pop())
    s.display()

    print("\n🔸 QUEUE DEMO")
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.display()
    print("Dequeued:", q.dequeue())
    q.display()

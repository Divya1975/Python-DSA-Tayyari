#  Practice Problems on Stack & Queue

#  Valid Parentheses (using Stack)
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
    return stack == []

print("Valid Parentheses:", is_valid_parentheses("({[]})"))  # ✅ True


#  Reverse a String using Stack
def reverse_string(string):
    stack = list(string)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

print("Reversed String:", reverse_string("hello"))  # ✅ olleh


# Queue using Two Stacks
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop() if self.out_stack else "Queue is empty"

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Dequeued:", q.dequeue())  #  1
print("Dequeued:", q.dequeue())  #  2


#  Check for Palindrome using Queue
from collections import deque

def is_palindrome(string):
    queue = deque(string)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

print("Is Palindrome:", is_palindrome("madam"))  #  True
print("Is Palindrome:", is_palindrome("hello"))  #  False

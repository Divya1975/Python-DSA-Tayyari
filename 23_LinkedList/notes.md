#  Linked List – Notes

## What is a Linked List?
A **Linked List** is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element (called a **node**) contains:
- The data
- A reference (or pointer) to the next node in the sequence

---

##  Node Structure

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

##  Key Terminology
Head: The first node in the list

Tail: The last node, which points to None

Pointer: Stores the reference to the next node

## Types of Linked Lists
Singly Linked List

Each node points to the next node only

Traversal is one-way

Doubly Linked List

Each node has two pointers (prev and next)

Can be traversed both ways

Circular Linked List

The last node points back to the first node

Can be singly or doubly circular


## Common Operations
traverse() – Visit each node from head to tail

insert_at_beginning(data) – Insert new node at the beginning

insert_at_end(data) – Append new node at the end

insert_after(prev_node, data) – Insert after a given node

delete_node(key) – Delete a node by value

search(key) – Search for a value

length() – Count the number of nodes

## Time Complexity

| Operation             | Singly Linked List |
| --------------------- | ------------------ |
| Insertion (beginning) | O(1)               |
| Insertion (end)       | O(n)               |
| Deletion (by value)   | O(n)               |
| Search                | O(n)               |
| Traversal             | O(n)               |


## Applications
Implementing stacks and queues

Navigation systems (forward/back)

Undo/redo functionality

Hash tables with chaining

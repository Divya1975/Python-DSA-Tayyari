"""
linkedlist_practice.py

Practice + interview-style utilities for a Singly Linked List.

Features:
- Insert at beginning/end
- Insert after value
- Delete by value
- Search
- Length
- Reverse (iterative & recursive)
- Get middle node
- Get Nth from end (two-pointer)
- Remove duplicates (unsorted)
- Detect cycle (Floyd)
- Merge two sorted linked lists (static method)
- Convert to / from Python list for easy testing

Run this file directly to see a demo.
"""


class Node:
    """Node of a singly linked list."""
    __slots__ = ("data", "next")

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List with common operations + interview helpers."""
    def __init__(self, iterable=None):
        self.head = None
        if iterable is not None:
            self.extend(iterable)

    # ------------------------------------------------------------------ #
    # Basic helpers
    # ------------------------------------------------------------------ #
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.length()

    def __repr__(self):
        return "LinkedList([" + ", ".join(repr(x) for x in self) + "])"

    # ------------------------------------------------------------------ #
    # Display / traversal
    # ------------------------------------------------------------------ #
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def to_list(self):
        return list(iter(self))

    @classmethod
    def from_list(cls, lst):
        return cls(lst)

    def extend(self, iterable):
        for item in iterable:
            self.insert_at_end(item)

    # ------------------------------------------------------------------ #
    # Insert operations
    # ------------------------------------------------------------------ #
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_value(self, target_data, data):
        current = self.head
        while current and current.data != target_data:
            current = current.next
        if current is None:
            print(f"{target_data} not found in the list.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # ------------------------------------------------------------------ #
    # Delete / search / length
    # ------------------------------------------------------------------ #
    def delete_node(self, key):
        current = self.head
        prev = None

        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"{key} not found in the list.")
            return

        if prev is None:  # delete head
            self.head = current.next
        else:
            prev.next = current.next

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # ------------------------------------------------------------------ #
    # Interview-style extras
    # ------------------------------------------------------------------ #
    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse(node, prev=None):
            if not node:
                return prev
            nxt = node.next
            node.next = prev
            return _reverse(nxt, node)

        self.head = _reverse(self.head)

    def get_middle(self):
        """
        Returns the middle node's data.
        If even length, returns the first of the two middles (fast-pointer method).
        Returns None if list is empty.
        """
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            if fast:  # move slow only when fast can move further or landed on last
                slow = slow.next
        return slow.data if slow else None

    def nth_from_end(self, n):
        """
        Return data of nth node from end (1-based).
        If n > length, return None.
        """
        fast = self.head
        for _ in range(n):
            if not fast:
                return None
            fast = fast.next

        slow = self.head
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.data if slow else None

    def remove_duplicates(self):
        """Remove duplicates from an unsorted linked list (O(n) extra space)."""
        seen = set()
        current = self.head
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def detect_cycle(self):
        """
        Floyd's cycle detection.
        Returns True if a cycle exists, else False.
        """
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    # ------------------------------------------------------------------ #
    # Static / utility algorithms
    # ------------------------------------------------------------------ #
    @staticmethod
    def merge_sorted(list1, list2):
        """
        Merge two *sorted* LinkedList objects into a new sorted LinkedList.
        Does not mutate the originals; builds new nodes.
        """
        p1 = list1.head
        p2 = list2.head
        merged = LinkedList()

        tail = None
        while p1 or p2:
            if p2 is None or (p1 is not None and p1.data <= p2.data):
                data = p1.data
                p1 = p1.next
            else:
                data = p2.data
                p2 = p2.next

            new_node = Node(data)
            if merged.head is None:
                merged.head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = tail.next

        return merged


# ---------------------------------------------------------------------- #
# Demo / quick tests
# ---------------------------------------------------------------------- #
def _demo_basic():
    print("\n--- Basic Ops Demo ---")
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_after_value(10, 15)
    ll.display()  # 5 -> 10 -> 15 -> 20 -> None
    print("Length:", ll.length())
    print("Search 15:", ll.search(15))
    ll.delete_node(10)
    ll.display()  # 5 -> 15 -> 20 -> None
    return ll


def _demo_reverse():
    print("\n--- Reverse Demo ---")
    ll = LinkedList([1, 2, 3, 4, 5])
    ll.display()
    ll.reverse_iterative()
    print("After reverse_iterative:")
    ll.display()
    ll.reverse_recursive()
    print("After reverse_recursive (back to original):")
    ll.display()


def _demo_middle_nth():
    print("\n--- Middle / Nth-from-End Demo ---")
    ll = LinkedList([10, 20, 30, 40, 50])
    ll.display()
    print("Middle:", ll.get_middle())
    for n in range(1, 7):
        print(f"{n}th from end:", ll.nth_from_end(n))


def _demo_remove_duplicates():
    print("\n--- Remove Duplicates Demo ---")
    ll = LinkedList([1, 2, 3, 2, 4, 3, 5, 1])
    ll.display()
    ll.remove_duplicates()
    print("After remove_duplicates:")
    ll.display()


def _demo_merge_sorted():
    print("\n--- Merge Sorted Lists Demo ---")
    l1 = LinkedList([1, 3, 5, 7])
    l2 = LinkedList([2, 4, 6, 8, 10])
    print("List 1:")
    l1.display()
    print("List 2:")
    l2.display()
    merged = LinkedList.merge_sorted(l1, l2)
    print("Merged:")
    merged.display()


if __name__ == "__main__":
    # Run demos when executed directly
    _demo_basic()
    _demo_reverse()
    _demo_middle_nth()
    _demo_remove_duplicates()
    _demo_merge_sorted()

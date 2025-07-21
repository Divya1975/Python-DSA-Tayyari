# linkedlist.py

class Node:
    """A node of a singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly Linked List implementation"""
    def __init__(self):
        self.head = None

    def display(self):
        """Prints all the elements in the list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_value(self, target_data, data):
        """Insert after a specific node value"""
        current = self.head
        while current and current.data != target_data:
            current = current.next

        if current is None:
            print(f"{target_data} not found in the list.")
            return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        """Deletes the first occurrence of the given key"""
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"{key} not found in the list.")
            return

        prev.next = current.next

    def search(self, key):
        """Search for a value in the list"""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def length(self):
        """Returns the total number of nodes"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_after_value(10, 15)
    ll.display()  # Output: 5 -> 10 -> 15 -> 20 -> None

    print("Length:", ll.length())  # Output: 4
    print("Search 15:", ll.search(15))  # Output: True

    ll.delete_node(10)
    ll.display()  # Output: 5 -> 15 -> 20 -> None

#  Tree Practice Questions

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#  1. Count the number of nodes in a binary tree
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

#  2. Find height of binary tree
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

#  3. Check if two trees are identical
def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 and root2 and root1.val == root2.val:
        return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)
    return False

#  4. Find sum of all nodes
def sum_of_nodes(root):
    if root is None:
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)

# Sample Tree 1:
#         10
#        /  \
#       5    15
#      / \     \
#     3   7     18

root1 = Node(10)
root1.left = Node(5)
root1.right = Node(15)
root1.left.left = Node(3)
root1.left.right = Node(7)
root1.right.right = Node(18)

# Sample Tree 2 (Identical to Tree 1)
root2 = Node(10)
root2.left = Node(5)
root2.right = Node(15)
root2.left.left = Node(3)
root2.left.right = Node(7)
root2.right.right = Node(18)

print("Total Nodes:", count_nodes(root1))
print("Height of Tree:", height(root1))
print("Sum of All Nodes:", sum_of_nodes(root1))
print("Are both trees identical?", is_identical(root1, root2))

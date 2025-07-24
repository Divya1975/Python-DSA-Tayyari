#  Tree - Basic Implementation in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#  Inorder Traversal (LNR)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

#  Preorder Traversal (NLR)
def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

#  Postorder Traversal (LRN)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

#  Level Order Traversal using Queue (BFS)
def level_order(root):
    if not root:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.data, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

#  Sample Tree:
#         A
#        / \
#       B   C
#      / \   \
#     D   E   F

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

print("Inorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
print("\nLevel Order Traversal:")
level_order(root)

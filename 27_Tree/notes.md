#  Tree - Notes

##  What is a Tree?
A **Tree** is a non-linear data structure that represents a hierarchical structure with a **root node** and child nodes forming a **tree-like structure**.

### Key Terms:
- **Node**: Each data element in the tree.
- **Root**: Topmost node of the tree.
- **Parent & Child**: A node that connects to other nodes below it.
- **Leaf**: A node with no children.
- **Subtree**: A tree formed by a node and its descendants.
- **Height**: Number of edges on the longest path from the node to a leaf.
- **Depth**: Number of edges from the root to that node.
- **Degree**: Number of children of a node.

---

##  Types of Trees:
1. **Binary Tree** – Each node has at most 2 children.
2. **Binary Search Tree (BST)** – Left < Root < Right
3. **Balanced Tree** – Height of left and right subtrees differ by at most 1.
4. **Complete Binary Tree** – All levels completely filled except possibly the last.
5. **Full Binary Tree** – Every node has 0 or 2 children.
6. **Perfect Binary Tree** – All internal nodes have 2 children and all leaves are at the same level.

---

##  Tree Traversal:
1. **Inorder (LNR)**  
   Left → Node → Right
2. **Preorder (NLR)**  
   Node → Left → Right
3. **Postorder (LRN)**  
   Left → Right → Node
4. **Level Order**  
   Traverse level by level using queue (BFS)

---

##  Tree Implementation:
- Usually implemented using **nodes and pointers**
- Each node is an object with:
  
  class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None
  

---

##  Applications of Tree:
- Storing hierarchical data (e.g. file system)
- Database indexing
- Expression parsing
- Decision-making algorithms (Decision Trees)
- Routing algorithms

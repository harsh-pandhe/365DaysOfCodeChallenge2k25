# 🎯 Day #69 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Binary trees are fascinating! 🌳 They form the backbone of many algorithms, from parsing expressions to optimizing databases. Today, I implemented **three fundamental tree traversal techniques**:  
✅ **Preorder (Root → Left → Right)**  
✅ **Inorder (Left → Root → Right)**  
✅ **Postorder (Left → Right → Root)**  

## 📚 What I Did Today  
I built a simple **Binary Tree** and implemented all three traversal methods using recursion. 🚀  

---

### 📝 **Binary Tree Traversal Implementation**  

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self.preorder_traversal(node.left, result) 
            self.preorder_traversal(node.right, result)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)  
            result.append(node.val) 
            self.inorder_traversal(node.right, result)  

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result) 
            self.postorder_traversal(node.right, result)  
            result.append(node.val)  

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

preorder_result, inorder_result, postorder_result = [], [], []
tree.preorder_traversal(tree.root, preorder_result)
tree.inorder_traversal(tree.root, inorder_result)
tree.postorder_traversal(tree.root, postorder_result)

print("Preorder Traversal:", preorder_result)
print("Inorder Traversal:", inorder_result)
print("Postorder Traversal:", postorder_result)
```

---

## 💡 Key Learnings  
✅ **Why Different Traversals?**  
- **Preorder**: Useful for copying trees and prefix expression evaluation.  
- **Inorder**: Retrieves sorted data from a BST.  
- **Postorder**: Used in deletion operations and postfix expression evaluation.  

✅ **Understanding the Order:**  
- **Preorder (DLR)**: Read data, traverse left, traverse right.  
- **Inorder (LDR)**: Traverse left, read data, traverse right.  
- **Postorder (LRD)**: Traverse left, traverse right, read data.  

---

## 🚀 Your Turn  
Try implementing **iterative** versions of these traversals using a stack! Can you optimize it further? 🤔  

#365DaysOfCode #CodingChallenge #BinaryTree #DataStructures #TreeTraversal  
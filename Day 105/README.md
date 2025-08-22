# 🎯 Day #105 of My 365 Days Coding Challenge

## 🌳 Complete Binary Tree Check

A **complete binary tree** is one where every level is fully filled, except possibly the last, and nodes are as far left as possible.
This project demonstrates how to **check if a binary tree is complete** using **Level Order Traversal (BFS)**.

---

## 📚 What I Did

* Implemented a function to check if a binary tree is complete.
* Used a **queue (BFS)** to traverse the tree level by level.
* Stopped adding children once a `None` was found, ensuring no nodes appear afterward.

---

## 📝 Python Implementation

```python
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_complete_tree(root):
    if not root:
        return True

    queue = deque([root])
    end = False

    while queue:
        node = queue.popleft()

        if node is None:
            end = True
        else:
            if end:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Is tree complete?", is_complete_tree(root))
```

---

## 💡 Key Learnings

✅ A complete binary tree **must be left-aligned**.

✅ BFS makes it easy to detect gaps in structure.

✅ Once a `None` child is seen, no more children should appear.

✅ **Time Complexity:** `O(n)` → efficient for large trees.

✅ Applications: **Heap construction, memory-efficient trees, tree balancing**.

---

## 🚀 Your Turn

* Extend the function to return the **index of the first violation**.
* Try visualizing the tree in a **binary heap array representation**.

---

`#365DaysOfCode` `#BinaryTree` `#CompleteTree` `#TreeTraversal` `#DataStructures` `#Python` `#AlgoLearning` `#InterviewPrep`
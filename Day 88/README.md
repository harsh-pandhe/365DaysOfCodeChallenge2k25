# 🎯 Day #88 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today I explored a deceptively simple yet crucial concept in tree-based data structures — **validating a Binary Search Tree (BST)**. 🌳
It’s not enough for just the left child to be less than the parent and the right to be greater; the entire **subtree must maintain the constraint** across all nodes.
This challenge reminded me how **global rules** matter more than **local appearances** — both in code and in life. 😉

---

## 📚 What I Did

✅ Implemented a recursive function to check whether a given **binary tree is a valid BST**.
✅ Used **min/max range validation** to enforce BST rules across subtrees.

---

## 📝 Python Code – Validate BST

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True

    if not (min_val < node.val < max_val):
        return False

    return (is_bst(node.left, min_val, node.val) and
            is_bst(node.right, node.val, max_val))
```

---

## 🌳 Example Tree  

```python
# Constructing this tree:
#        10
#       /  \
#      5   15
#          / \
#        12  20

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(20)

print("Is BST?", is_bst(root))
```

---

## 💡 Key Learnings

* ✅ **BST Rule:** All nodes in the left subtree must be `< root`, and all in the right must be `> root`.
* ✅ Simple child checks aren’t enough — **validate using a range** across the subtree.
* ✅ Use **recursion** with `min` and `max` bounds to track the valid value range.
* ✅ Time Complexity: **O(n)** — each node is visited once.
* ✅ Common Mistake: Only comparing `node.left.val < node.val < node.right.val`, which doesn’t catch deep violations.

---

## 🚀 Your Turn

* 🛠️ Modify the function to return the **first node that violates** the BST property.
* 🔍 Count the **total number of violations** in a tree.
* 🌲 Implement an **iterative version** using stack instead of recursion.

---

\#365DaysOfCode #BinarySearchTree #BSTValidation #TreeAlgorithms #Python #DataStructures #Recursion #GraphTheory

---
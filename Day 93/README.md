# 🎯 Day #93 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today I flipped the script—quite literally!
I implemented a function to **invert a binary tree**, meaning I **swapped every left and right child recursively**.
This is one of those visually satisfying challenges that shows how **recursion can transform structures with minimal code**.

It’s also symbolic: sometimes, a shift in perspective reveals things you couldn't see before. 😉

---

## 📚 What I Did

Built a simple and elegant function to:

* Invert (mirror) a binary tree 🌳
* Traverse and print the tree using **inorder traversal** before and after inversion

---

## 📝 Python Code – Invert a Binary Tree

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def invert_tree(node):
    if node is None:
        return None

    node.left, node.right = invert_tree(node.right), invert_tree(node.left)
    return node

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=' ')
        inorder_traversal(node.right)
```

---

## ▶️ Example Usage

```python
# Constructing the tree:
#        1
#      /   \
#     2     3
#    / \   / \
#   4  5  6   7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Original Tree (Inorder):")
inorder_traversal(root)

invert_tree(root)

print("\nInverted Tree (Inorder):")
inorder_traversal(root)
```

---

## 💡 Key Learnings

* ✅ **Tree inversion** is a classic **recursive pattern**.
* ✅ Each node is **visited once** → Time Complexity: **O(n)**
* ✅ Great practice for:

  * Tree recursion
  * Divide and conquer techniques
  * Understanding structure manipulation
* ✅ Real-world applications:

  * **Image processing**
  * **Symmetry checks**
  * **Data structure transformations**
  * Fun fact: This was a **Google interview question**!

---

## 🚀 Your Turn

Try extending this to:

* Implement **iterative inversion using BFS (queue)**
* Invert only **alternate levels** of a perfect binary tree
* Return a **new inverted tree** without mutating the original

---

`#365DaysOfCode` `#InvertTree` `#MirrorBinaryTree` `#TreeRecursion` `#DataStructures` `#Python` `#InterviewPrep`

---
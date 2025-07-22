# 🎯 Day #96 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today’s challenge was about finding the **Lowest Common Ancestor (LCA)** of two nodes in a binary tree — a deceptively simple problem with **profound applications**.

What I loved most about it was the **recursive elegance** and how it uncovers the **first point of convergence** between two nodes — a valuable analogy in life and logic. 🌿

---

## 📚 What I Did

I implemented a recursive function to determine the **lowest node in a binary tree that is an ancestor to both target nodes**.

---

## 📝 Python Code – Lowest Common Ancestor (LCA)

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right
```

---

## 🌲 Example Tree

```plaintext
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

```python
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

p = root.left             # Node 5
q = root.left.right.right # Node 4

ancestor = lowest_common_ancestor(root, p, q)
print("Lowest Common Ancestor:", ancestor.val)  # Output: 5
```

---

## 💡 Key Learnings

* ✅ The **Lowest Common Ancestor** is the first node where paths to `p` and `q` split.
* ✅ No need for parent pointers or additional data structures.
* ✅ Time complexity: **O(n)** in worst case (where `n` = number of nodes).
* ✅ Important for:

  * 📁 Folder hierarchies
  * 🧬 Genealogical trees
  * 🧠 AI decision trees
  * 🛰️ Network routing systems

---

## 🚀 Your Turn

* Modify the function to **find LCA in a Binary Search Tree (BST)** for improved efficiency (O(log n)).
* Return **distance from root to LCA**, or **depth of both nodes from LCA**.
* Extend to handle **multiple queries efficiently** using preprocessing.

---

`#365DaysOfCode` `#LCA` `#BinaryTree` `#TreeAlgorithms` `#Recursion` `#InterviewPrep` `#DataStructures`

---
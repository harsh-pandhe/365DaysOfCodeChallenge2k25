# 🎯 Day #92 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today’s challenge was all about **comparing two binary trees** — not just for data, but for structure as well.
It’s a task that showcases the **power of recursion** in dealing with naturally recursive data structures like trees 🌳.

A tree is like a fingerprint — if both structure and content match, they’re identical. If even one part is different, the identity changes.

---

## 📚 What I Did

✅ Wrote a **recursive function** to compare:

* 🔁 **Structure** (the shape of the trees)
* 🔢 **Values** (data at each node)

✅ Compared nodes depth-first (DFS) using recursion.

---

## 📝 Python Code – Check If Two Binary Trees Are Identical

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def are_identical(tree1, tree2):
    if not tree1 and not tree2:
        return True

    if not tree1 or not tree2:
        return False

    return (tree1.val == tree2.val and
            are_identical(tree1.left, tree2.left) and
            are_identical(tree1.right, tree2.right))
```

---

## ▶️ Example Usage

```python
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print("Are the trees identical?", are_identical(root1, root2))  # Output: True
```

---

## 💡 Key Learnings

* ✅ The **order** and **value** at each node must match.
* ✅ Recursion naturally fits the tree structure.
* ✅ Time Complexity: **O(n)**, where `n` is the number of nodes.
* ✅ Practical applications:

  * File/directory comparison tools
  * Version control tree diffs
  * Expression trees in compilers

---

## 🚀 Your Turn

🔧 Enhance the function to:

* Return the **first mismatching node value or level**
* Provide a **reason for inequality**
* Or return the **difference subtree**

---

`#365DaysOfCode` `#BinaryTree` `#TreeComparison` `#Recursion` `#CodingChallenge` `#DataStructures` `#Python`

---

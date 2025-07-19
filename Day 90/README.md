# 🎯 Day #90 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today I tackled the **diameter of a binary tree** — the **longest path between any two nodes**.
This challenge reminded me that in trees (and life), the **longest journeys aren’t always top-down**; they may stretch across in unseen but meaningful paths. 🌿

It was an excellent exercise in **recursive depth-first traversal**, and in how to manage multiple return values like **height and diameter** simultaneously.

---

## 📚 What I Did

✅ Implemented the **diameter finder** using **post-order DFS**.
✅ Computed both height and updated the global maximum diameter during recursion.

---

## 📝 Python Code – Diameter of Binary Tree

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def diameter_of_binary_tree(root):
    diameter = [0]

    def height(node):
        if not node:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        diameter[0] = max(diameter[0], left_height + right_height)

        return 1 + max(left_height, right_height)

    height(root)
    return diameter[0]
```

---

## 🌳 Example Tree

```python
#        1
#       / \
#      2   3
#     / \     
#    4   5    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Diameter of the binary tree:", diameter_of_binary_tree(root))  # Output: 3
```

---

## 💡 Key Learnings

* ✅ **Diameter** is the longest path between any two nodes (in terms of edges or nodes).
* ✅ It **may or may not pass through the root**.
* ✅ Use **post-order DFS** to gather **left and right subtree heights**.
* ✅ Time complexity: **O(n)** – we visit each node once.
* ✅ Great example of using recursion to compute **multiple properties** at once.

---

## 🚀 Your Turn

* 🔁 Modify this to **return the actual longest path** instead of just the length.
* 🔄 Try the same logic on an **N-ary tree**.
* 🧩 Apply the concept to find the **diameter of a weighted graph/tree**.

---

`#365DaysOfCode` `#BinaryTree` `#TreeTraversal` `#Diameter` `#Recursion` `#DFS` `#InterviewPrep` `#DataStructures` `#Python`

---

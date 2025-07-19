# 🎯 Day #89 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today, I implemented the **Level Order Traversal** of a binary tree 🌳 — also known as **Breadth-First Search (BFS)**.
This algorithm reflects how we often learn: level by level, concept by concept. It’s widely used in **network traversal**, **AI decision trees**, and **shortest path problems**.

Building this from scratch with a queue helped me visualize and appreciate the layered nature of BFS.

---

## 📚 What I Did

✅ Implemented **Level Order Traversal** in Python using a queue.
✅ Printed each level of a binary tree from top to bottom, left to right.

---

## 📝 Python Code – Level Order Traversal (BFS)

```python
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

---

## 🌳 Example Tree

```python
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

output = level_order_traversal(root)
for i, level in enumerate(output):
    print(f"Level {i+1}: {level}")
```

### ✅ Output:

```
Level 1: [1]
Level 2: [2, 3]
Level 3: [4, 5, 6, 7]
```

---

## 💡 Key Learnings

* ✅ **Level Order Traversal** = **Breadth-First Search (BFS)** for trees.
* ✅ Uses a **queue** to manage nodes level by level.
* ✅ Time Complexity: **O(n)** where `n` is the number of nodes.
* ✅ Applications include:

  * 🌐 **Network broadcasting**
  * 🧠 **AI decision trees**
  * 🛠️ **Serialization and deserialization**
  * 🧭 **Shortest path in unweighted graphs**

---

## 🚀 Your Turn

* 🔁 Modify to print each level **on a new line**.
* 🔄 Implement **Zigzag Level Order Traversal** (alternating left-to-right and right-to-left).
* 🌟 Try **bottom-up level order traversal** (start from the leaves).

---

`#365DaysOfCode` `#TreeTraversal` `#BinaryTree` `#BFS` `#LevelOrder` `#DataStructures` `#Algorithms` `#Python`

---
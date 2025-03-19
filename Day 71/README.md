# 🎯 Day #71 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Binary trees continue to amaze me 🌳. Today, I focused on calculating the **height** of a binary tree—a fundamental concept that influences operations like balancing, searching, and traversal efficiency.  

## 📚 What I Did Today  
I implemented a function to find the **height of a binary tree** using **recursion**. The height of a tree is the number of edges on the longest path from the root to a leaf node.  

---

### 📝 **Finding the Height of a Binary Tree**  

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_height(root):
    if not root:
        return -1
    
    left_height = find_height(root.left)
    right_height = find_height(root.right)

    return max(left_height, right_height) + 1

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.right = Node(6)
tree.right.right.right = Node(7)

print("Height of the tree:", find_height(tree))
```

---

## 💡 Key Learnings  
✅ **Understanding Tree Height:**  
- **Height of a tree** is the longest path from the root to a leaf.  
- **A single-node tree has a height of 0** since it has no edges.  

✅ **Optimized Approach:**  
- This **recursive approach** ensures an **O(N)** time complexity, where **N** is the number of nodes.  
- Uses **Depth-First Search (DFS)** to traverse the tree efficiently.  

---

## 🚀 Your Turn  
Try implementing an **iterative approach** using **level-order traversal (BFS)** to calculate height!  

#365DaysOfCode #CodingChallenge #BinaryTree #TreeHeight #Algorithms  
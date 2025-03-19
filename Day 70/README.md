# 🎯 Day #70 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Today’s challenge took me deeper into **binary trees** 🌳. I explored **balanced binary trees**, a crucial concept in optimizing search performance. An **unbalanced tree** can degrade into a linked list, making operations inefficient.  

## 📚 What I Did Today  
I implemented a function to check if a **binary tree is balanced**, meaning the height difference between left and right subtrees is at most **1**.  

---

### 📝 **Checking If a Binary Tree is Balanced**  

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return check_height(root) != -1

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.right = Node(6)
tree.right.right.right = Node(7) 

print("Is the tree balanced?", is_balanced(tree))
```

---

## 💡 Key Learnings  
✅ **What is a Balanced Tree?**  
- A **balanced binary tree** ensures that no subtree is too deep compared to others.  
- A tree is **balanced** if the height difference between left and right subtrees is at most **1**.  

✅ **Efficient Approach:**  
- A naive approach calculates height separately for each node, making it **O(N²)** in worst cases.  
- The **optimized approach** (used here) computes height **on the fly** in **O(N)** time. 🚀  

---

## 🚀 Your Turn  
Try implementing a **self-balancing tree (AVL Tree or Red-Black Tree)** to maintain balance automatically!  

#365DaysOfCode #CodingChallenge #BinaryTree #BalancedTree #Algorithms  
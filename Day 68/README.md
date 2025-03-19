# 🎯 Day #68 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Trees are everywhere in programming—from databases to search engines! 🌳 Today, I took on the challenge of **implementing a Binary Search Tree (BST)**, a fundamental data structure that enables fast searching, insertion, and deletion. 🚀  

## 📚 What I Did Today  
I built a **BST from scratch** in Python, implementing:  
✅ **Insertion** of elements  
✅ **Inorder Traversal** (which prints elements in sorted order)  
✅ **Search** functionality  

---

### 📝 **Binary Search Tree (BST) Implementation**  

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, root, result):
        if root:
            self._inorder_helper(root.left, result)
            result.append(root.val)
            self._inorder_helper(root.right, result)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

bst = BST()
for num in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(num)

print("Inorder Traversal:", bst.inorder_traversal())
print("Search 40:", "Found" if bst.search(40) else "Not Found")
```

---

## 💡 Key Learning  
✅ **Why Use a BST?**  
- Efficient **O(log n)** search, insertion, and deletion. 🔍  
- Forms the basis for advanced data structures like AVL trees and Red-Black trees.  

✅ **How It Works:**  
- Each node follows the **left < root < right** rule.  
- **Inorder traversal** gives a sorted sequence of elements.  

✅ **Future Enhancements:**  
- Add **deletion** operation.  
- Convert it into a **self-balancing** BST (e.g., AVL Tree).  

---

## 🚀 Your Turn  
Modify the code to **delete nodes** from the BST. Can you implement a **balanced BST**? 🤔  

#365DaysOfCode #CodingChallenge #BST #DataStructures #BinarySearchTree  
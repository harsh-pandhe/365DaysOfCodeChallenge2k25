# 🌳 Maximum Path Sum in a Binary Tree

### 🎯 Day #108 of My 365 Days Coding Challenge!

---

## 💭 Reflection

Today’s challenge was about finding the **maximum path sum** in a binary tree — where a path can start and end at *any* node.

It was an interesting mix of **recursion, dynamic programming, and edge-case handling**.
What stood out to me is that sometimes, negative values in subtrees need to be **ignored**, because they drag down the sum — just like in life, sometimes we let go of burdens to reach greater heights. ✨

---

## 📚 What I Did

* ✅ Implemented a **recursive DFS solution**.
* ✅ Used **post-order traversal** to calculate contributions bottom-up.
* ✅ Ignored **negative branch sums** that don’t help the path.
* ✅ Achieved **O(n)** time complexity.

---

## 📝 Code

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def max_path_sum(self, root):
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            current_sum = node.val + left + right

            self.max_sum = max(self.max_sum, current_sum)

            return node.val + max(left, right)

        dfs(root)
        return self.max_sum


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print("Maximum Path Sum:", sol.max_path_sum(root))
```

---

## 💡 Key Learnings

* Paths can start and end **anywhere**, not just from root to leaf.
* Negative branch sums are **ignored**.
* Post-order DFS makes it possible to calculate contributions bottom-up.
* **Time Complexity:** `O(n)` where *n* = number of nodes.

---

## 🚀 Challenge Yourself

* ➕ Modify code to return the **actual path** along with the sum.
* 💬 Print contribution values at every node.
* 🔁 Restrict it to **root-to-leaf paths only** and compare results.

---

\#365DaysOfCode #BinaryTree #MaxPathSum #DynamicProgramming #Recursion #Python #DSA #Algorithms #InterviewPrep

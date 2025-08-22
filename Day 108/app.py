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

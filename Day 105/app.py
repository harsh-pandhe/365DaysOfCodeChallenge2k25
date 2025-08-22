from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_complete_tree(root):
    if not root:
        return True

    queue = deque([root])
    end = False

    while queue:
        node = queue.popleft()

        if node is None:
            end = True
        else:
            if end:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Is tree complete?", is_complete_tree(root))

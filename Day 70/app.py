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

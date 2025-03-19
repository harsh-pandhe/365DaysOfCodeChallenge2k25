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

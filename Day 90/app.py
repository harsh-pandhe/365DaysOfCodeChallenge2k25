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


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Diameter of the binary tree:", diameter_of_binary_tree(root))

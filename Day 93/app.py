class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def invert_tree(node):
    if node is None:
        return None

    node.left, node.right = invert_tree(node.right), invert_tree(node.left)
    return node


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)


# Constructing the tree:
#        1
#      /   \
#     2     3
#    / \   / \
#   4  5  6   7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Original Tree (Inorder):")
inorder_traversal(root)

invert_tree(root)

print("\nInverted Tree (Inorder):")
inorder_traversal(root)

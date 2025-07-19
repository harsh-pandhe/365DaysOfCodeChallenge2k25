class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_bst(node, min_val=float("-inf"), max_val=float("inf")):
    if node is None:
        return True

    if not (min_val < node.val < max_val):
        return False

    return is_bst(node.left, min_val, node.val) and is_bst(
        node.right, node.val, max_val
    )


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(20)

print("Is BST?", is_bst(root))

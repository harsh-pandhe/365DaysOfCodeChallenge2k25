class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def are_identical(tree1, tree2):
    if not tree1 and not tree2:
        return True

    if not tree1 or not tree2:
        return False

    return (
        tree1.val == tree2.val
        and are_identical(tree1.left, tree2.left)
        and are_identical(tree1.right, tree2.right)
    )


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print("Are the trees identical?", are_identical(root1, root2))

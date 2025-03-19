class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.val)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

preorder_result, inorder_result, postorder_result = [], [], []
tree.preorder_traversal(tree.root, preorder_result)
tree.inorder_traversal(tree.root, inorder_result)
tree.postorder_traversal(tree.root, postorder_result)

print("Preorder Traversal:", preorder_result)
print("Inorder Traversal:", inorder_result)
print("Postorder Traversal:", postorder_result)

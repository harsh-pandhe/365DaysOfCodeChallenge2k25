class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root

    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, root, result):
        if root:
            self._inorder_helper(root.left, result)
            result.append(root.val)
            self._inorder_helper(root.right, result)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)


bst = BST()
for num in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(num)

print("Inorder Traversal:", bst.inorder_traversal())
print("Search 40:", "Found" if bst.search(40) else "Not Found")

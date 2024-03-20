# I am doing database indexing here

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

def build_index(names):
    bst = BST()
    for name in names:
        bst.insert(name)
    return bst

def search_name(bst, name):
    node = bst.search(name)
    if node:
        print(f"Name '{name}' found in index.")
    else:
        print(f"Name '{name}' not found in index.")

def delete_name(bst, name):
    bst.delete(name)
    print(f"Name '{name}' deleted from index.")

# Sample data
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

# Build the index
index = build_index(names)

# Search for a name
search_name(index, "Alice")
search_name(index, "John")

# Delete a name
delete_name(index, "Bob")
search_name(index, "Bob")

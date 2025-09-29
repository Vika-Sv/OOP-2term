from my_string import MyString

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data.value < node.data.value:
            if node.left == None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def inorder(self, node=None):
        if node == None:
            node = self.root
        if node.left:
            self.inorder(node.left)
        print(node.data.display())
        if node.right:
            self.inorder(node.right)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if str(value.value) < str(current.value.value):
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return []
        result = []
        if node.left:
            result += self.postorder(node.left)
        if node.right:
            result += self.postorder(node.right)
        result.append(node.value)
        return result

def menu_tree():
    from ryadok import Ryadok
    tree = BinaryTree()
    while True:
        print("\n--- Дерево ---")
        print("1. Додати рядок")
        print("2. Postorder")
        print("0. Вихід")
        choice = input("Вибір: ")

        if choice == "1":
            txt = input("Рядок: ")
            tree.insert(Ryadok(txt))
        elif choice == "2":
            for r in tree.postorder():
                print(r.value)
        elif choice == "0":
            break

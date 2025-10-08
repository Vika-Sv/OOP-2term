from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value
        self.left: Optional['Node[T]'] = None
        self.right: Optional['Node[T]'] = None

class BinaryTree(Generic[T]):
    def __init__(self):
        self.root: Optional[Node[T]] = None

    def insert(self, value: T):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node: Node[T], value: T):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

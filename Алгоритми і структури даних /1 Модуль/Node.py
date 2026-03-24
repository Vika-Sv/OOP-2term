class Node:
    """Вузол зв'язного стека."""
    def __init__(self, data: int, next_node=None):
        self.data = data
        self.next = next_node
 
 

class LinkedStack:
    def __init__(self):
        self._top = None  # вершина стека
 
    def is_empty(self) -> bool:
        """Перевіряє, чи стек порожній (top is None)."""
        return self._top is None
 
    def push(self, value: int):
        """Додає елемент на вершину стека."""
        self._top = Node(value, self._top)
 
    def pop(self) -> int:
        """Знімає та повертає елемент з вершини стека."""
        if self.is_empty():
            raise IndexError("[LinkedStack] Стек порожній!")
        value = self._top.data
        self._top = self._top.next
        return value
 
    def peek(self) -> int:
        """Повертає елемент з вершини без видалення."""
        if self.is_empty():
            raise IndexError("[LinkedStack] Стек порожній!")
        return self._top.data
 
    def print(self):
        elements = []
        current = self._top
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(f"[LinkedStack] Стек (вершина -> дно): [{', '.join(elements)}]") 
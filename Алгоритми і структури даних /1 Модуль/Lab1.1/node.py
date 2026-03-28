class _Node:
    def __init__(self, data: int, next__Node=None):
        self.data = data
        self.next = next__Node
 
 

class LinkedStack:
    def __init__(self):
        self._top = None  # вершина стека
 
    def is_empty(self) -> bool:
        return self._top is None
 
    def push(self, value: int):
        self._top = _Node(value, self._top)
 
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("[LinkedStack] Стек порожній!")
        value = self._top.data
        self._top = self._top.next
        return value
 
    def peek(self) -> int:
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
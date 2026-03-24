class VectorList:
    def __init__(self, capacity: int):
        self._data = [None] * capacity
        self._size = 0
 
    def is_full(self) -> bool:
        """Перевіряє, чи список повний."""
        return self._size == len(self._data)
 
    def is_empty(self) -> bool:
        """Перевіряє, чи список порожній."""
        return self._size == 0
 
    def add(self, value: int) -> bool:
        """Вставляє елемент у кінець списку. Повертає True при успіху."""
        if self.is_full():
            print(f"[VectorList] Список повний! Не можна додати: {value}")
            return False
        if value <= 0:
            print(f"[VectorList] Елемент має бути додатним! Відхилено: {value}")
            return False
        self._data[self._size] = value
        self._size += 1
        return True
 
    def remove(self, index: int) -> int:
        """Видаляє елемент за індексом зі зсувом вліво. Повертає видалений елемент."""
        if self.is_empty():
            raise IndexError("[VectorList] Список порожній!")
        if index < 0 or index >= self._size:
            raise IndexError(f"[VectorList] Невірний індекс: {index}")
        removed = self._data[index]
        # Зсув елементів вліво
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return removed
 
    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError(f"[VectorList] Невірний індекс: {index}")
        return self._data[index]
 
    def size(self) -> int:
        return self._size
 
    def print(self):
        elements = [str(self._data[i]) for i in range(self._size)]
        print(f"[VectorList] Список ({self._size} елем.): [{', '.join(elements)}]")
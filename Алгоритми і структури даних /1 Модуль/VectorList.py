class VectorList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity  # Емуляція масиву фіксованого розміру
        self.count = 0

    def isFull(self):
        return self.count == self.capacity

    def isEmpty(self):
        return self.count == 0

    def insert(self, value):
        # Перевірка: чи це рядок, що містить ціле додатне число
        if not (isinstance(value, str) and value.isdigit() and int(value) > 0):
            print(f"Помилка: '{value}' не є додатним цілим числом у форматі рядка.")
            return False
        
        if self.isFull():
            print("Список заповнений!")
            return False
        
        self.items[self.count] = value
        self.count += 1
        return True

    def remove_at(self, index):
        if self.isEmpty() or index < 0 or index >= self.count:
            raise IndexError("Видалення неможливе: некоректний індекс або порожній список.")
        
        removed_item = self.items[index]
        # Зсув елементів вліво
        for i in range(index, self.count - 1):
            self.items[i] = self.items[i+1]
        
        self.items[self.count - 1] = None
        self.count -= 1
        return removed_item

    def display(self):
        print("Вміст списку:", self.items[:self.count])
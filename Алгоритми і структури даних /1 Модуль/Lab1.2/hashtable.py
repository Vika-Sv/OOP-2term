from rectangle import Rectangle

class _Deleted:
    def __str__(self):
        return "[видалено]"
 
DELETED = _Deleted()
 

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # None = порожньо
 
    # Основна хеш-функція (метод ділення)
    def h1(self, key):
        return key % self.size
 
    # Допоміжна хеш-функція (для подвійного хешування)
    def h2(self, key):
        return 1 + (key % (self.size - 1))
 
    # Позиція при i-му зондуванні
    def probe(self, key, i):
        return (self.h1(key) + i * self.h2(key)) % self.size
 
    def insert(self, rect):
        key = rect.key()
        for i in range(self.size):
            pos = self.probe(key, i)
            if self.table[pos] is None or isinstance(self.table[pos], _Deleted):
                self.table[pos] = rect
                return True
        return False  # таблиця повна
 
    def delete_by_area(self, threshold):
        count = 0
        for i in range(self.size):
            cell = self.table[i]
            if isinstance(cell, Rectangle) and cell.area() < threshold:
                self.table[i] = DELETED
                count += 1
        return count
 
    def display(self):
        print(f"\n{'─'*60}")
        print(f"{'Поз':>4}  {'Ключ':>6}  {'Елемент'}")
        print(f"{'─'*60}")
        for i, cell in enumerate(self.table):
            if cell is None:
                print(f"{i:>4}  {'—':>6}  [порожньо]")
            else:
                key = cell.key() if isinstance(cell, Rectangle) else "—"
                print(f"{i:>4}  {str(key):>6}  {cell}")
        print(f"{'─'*60}\n")
 
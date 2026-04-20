from rectangle import Rectangle
from hashtable import HashTable

def main():
    size = int(input("Введіть розмір хеш-таблиці: "))
    ht = HashTable(size)
 
    print(f"\nВставляємо {size} прямокутників:\n")
    for _ in range(size):
        rect = Rectangle.random_rectangle()
        ok = ht.insert(rect)
        status = "Вставлено" if ok else "Таблиця повна"
        print(f"  {status}: ключ={rect.key():>4}  {rect}")
 
    print("\nТаблиця ДО видалення:")
    ht.display()
 
    threshold = float(input("Введіть поріг площі (видалити всі з S < порогу): "))
    removed = ht.delete_by_area(threshold)
    print(f"\nВидалено {removed} елемент(ів) із площею < {threshold}")
 
    print("\nТаблиця ПІСЛЯ видалення:")
    ht.display()
 
 
if __name__ == "__main__":
    main()
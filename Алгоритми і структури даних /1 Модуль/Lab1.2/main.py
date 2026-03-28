from rectangle import Rectangle
from hashtable import HashTable

def main():
    # 1. Створити хеш-таблицю заданого розміру
    size = int(input("Введіть розмір хеш-таблиці: "))
    ht = HashTable(size)
 
    # 2. Вставити елементи з урахуванням колізій
    print(f"\nВставляємо {size} прямокутників:\n")
    for _ in range(size):
        rect = Rectangle.random_rectangle()
        ok = ht.insert(rect)
        status = "✔ Вставлено" if ok else "✘ Таблиця повна"
        print(f"  {status}: ключ={rect.key():>4}  {rect}")
 
    # 3. Вивести вміст таблиці
    print("\nТаблиця ДО видалення:")
    ht.display()
 
    # 4. Видалити елементи за критерієм і вивести таблицю
    threshold = float(input("Введіть поріг площі (видалити всі з S < порогу): "))
    removed = ht.delete_by_area(threshold)
    print(f"\nВидалено {removed} елемент(ів) із площею < {threshold}")
 
    print("\nТаблиця ПІСЛЯ видалення:")
    ht.display()
 
 
if __name__ == "__main__":
    main()
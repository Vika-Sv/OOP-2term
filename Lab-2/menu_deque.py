from ryadok import Ryadok
from collections import deque

def menu_deque():
    d = deque()
    while True:
        print("\n--- Deque ---")
        print("1. Додати")
        print("2. Оновити")
        print("3. Видалити")
        print("4. Пошук")
        print("5. Вставка")
        print("6. Заміна")
        print("7. Вивести всі")
        print("0. Вихід")
        choice = input("Вибір: ")

        if choice == "1":
            txt = input("Рядок: ")
            d.append(Ryadok(txt))
        elif choice == "2":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(d):
                d[idx].value = input("Новий рядок: ")
                d[idx].length = len(d[idx].value)
        elif choice == "3":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(d):
                del d[idx]
        elif choice == "4":
            sub = input("Підрядок: ")
            for r in d:
                print(r.value, "->", "Знайдено" if r.search(sub) else "Не знайдено")
        elif choice == "5":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(d):
                sub = input("Що вставити: ")
                pos = int(input("Позиція: "))
                d[idx].insert(sub, pos)
        elif choice == "6":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(d):
                old = input("Що замінити: ")
                new = input("На що: ")
                d[idx].replace(old, new)
        elif choice == "7":
            for r in d:
                print(r.value)
        elif choice == "0":
            break

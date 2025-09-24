from ryadok import Ryadok

def menu_list():
    lst = []
    while True:
        print("\n--- List ---")
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
            lst.append(Ryadok(txt))
        elif choice == "2":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(lst):
                lst[idx].value = input("Новий рядок: ")
                lst[idx].length = len(lst[idx].value)
        elif choice == "3":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(lst):
                del lst[idx]
        elif choice == "4":
            sub = input("Підрядок: ")
            for r in lst:
                print(r.value, "->", "Знайдено" if r.search(sub) else "Не знайдено")
        elif choice == "5":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(lst):
                sub = input("Що вставити: ")
                pos = int(input("Позиція: "))
                lst[idx].insert(sub, pos)
        elif choice == "6":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(lst):
                old = input("Що замінити: ")
                new = input("На що: ")
                lst[idx].replace(old, new)
        elif choice == "7":
            for r in lst:
                print(r.value)
        elif choice == "0":
            break

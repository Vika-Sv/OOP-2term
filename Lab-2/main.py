import array
from my_string import MyString
from binary_tree import BinaryTree

def main():
    objs = []      
    arr = array.array('i') 
    tree = BinaryTree()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Додати рядок")
        print("2. Видалити рядок")
        print("3. Оновити рядок")
        print("4. Пошук рядка у списку")
        print("5. Показати всі рядки")
        print("6. Операції над рядком")
        print("7. Масив довжин")
        print("8. Побудувати дерево")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            val = input("Введіть рядок: ")
            obj = MyString(val)
            objs.append(obj)
            arr.append(obj.length)
            print("Додано!")

        elif choice == "2":
            idx = int(input("Введіть індекс: "))
            if idx >= 0 and idx < len(objs):
                del objs[idx]
                arr = array.array('i', [o.length for o in objs])
                print("Видалено!")
            else:
                print("Невірний індекс!")

        elif choice == "3":
            idx = int(input("Введіть індекс: "))
            if idx >= 0 and idx < len(objs):
                new_val = input("Нове значення: ")
                objs[idx] = MyString(new_val)
                arr = array.array('i', [o.length for o in objs])
                print("Оновлено!")
            else:
                print("Невірний індекс!")

        elif choice == "4":
            search_val = input("Що шукаємо: ")
            found = None
            for o in objs:
                if search_val in o.value:
                    found = o
                    break
            if found:
                print("Знайдено:", found.display())
            else:
                print("Не знайдено!")

        elif choice == "5":
            if objs:
                for i, o in enumerate(objs):
                    print(i, ":", o.display(), "(довжина", o.length, ")")
            else:
                print("Список порожній")

        elif choice == "6":
            idx = int(input("Виберіть індекс: "))
            if idx >= 0 and idx < len(objs):
                obj = objs[idx]
                print("1. Пошук підрядка")
                print("2. Вставка підрядка")
                print("3. Заміна підрядка")
                sub_choice = input("Ваш вибір: ")
                if sub_choice == "1":
                    sub = input("Підрядок: ")
                    pos = obj.find_substring(sub)
                    print("Знайдено:", pos if pos != -1 else "Не знайдено")
                elif sub_choice == "2":
                    sub = input("Що вставити: ")
                    pos = int(input("Позиція: "))
                    obj.insert_substring(sub, pos)
                    print("Новий рядок:", obj.display())
                elif sub_choice == "3":
                    old = input("Що замінити: ")
                    new = input("На що замінити: ")
                    obj.replace_substring(old, new)
                    print("Новий рядок:", obj.display())
            else:
                print("Невірний індекс!")

        elif choice == "7":
            print("Масив довжин:", list(arr))

        elif choice == "8":
            tree = BinaryTree()
            for o in objs:
                tree.insert(o)
            print("Обхід дерева:")
            tree.inorder()

        elif choice == "0":
            break

        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()

import array

def menu_array():
    arr = array.array('u')
    while True:
        print("\n--- Array ---")
        print("1. Додати символ")
        print("2. Оновити символ")
        print("3. Видалити символ")
        print("4. Пошук символа")
        print("5. Вивести всі")
        print("0. Вихід")
        choice = input("Вибір: ")

        if choice == "1":
            c = input("Символ: ")
            if len(c) == 1:
                arr.append(c)
        elif choice == "2":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(arr):
                c = input("Новий символ: ")
                if len(c) == 1:
                    arr[idx] = c
        elif choice == "3":
            idx = int(input("Індекс: "))
            if 0 <= idx < len(arr):
                arr.pop(idx)
        elif choice == "4":
            c = input("Символ: ")
            print("Знайдено" if c in arr else "Не знайдено")
        elif choice == "5":
            print(list(arr))
        elif choice == "0":
            break

from vectorlist import VectorList
from node import Node
from node import LinkedStack


def main():
    # --- Крок 1: створення екземплярів обох структур даних ---
    list1 = VectorList(12)
    stack = LinkedStack()
 
    # --- Крок 2: вставка елементів до списку та виведення ---
    print("=== КРОК 1-2: Вставка елементів до списку ===")
    values = [15, 63, 42, 71, 8, 99, 50, 57, 100, 33, 81, 4]
    for v in values:
        list1.add(v)
 
    print("Початковий стан списку: ", end="")
    list1.print()
 
    # --- Крок 3: формування стека згідно із завданням ---
    # Переміщуємо зі списку непарні елементи > 50 до стека
    print()
    print("=== КРОК 3: Переміщення непарних > 50 зі списку до стека ===")
 
    i = 0
    while i < list1.size():
        val = list1.get(i)
        if val % 2 != 0 and val > 50:
            list1.remove(i)   # зсув вліво вбудований у remove()
            stack.push(val)
            print(f"  Переміщено: {val}")
            # i не збільшуємо — після видалення на цій позиції новий елемент
        else:
            i += 1
 
    # --- Крок 4: виведення вмісту обох структур ---
    print()
    print("=== КРОК 4: Вміст обох структур даних ===")
    print("Перша структура  — ", end="")
    list1.print()
    print("Друга структура  — ", end="")
    stack.print()
 
    # --- Демонстрація захисту від порожнього стека ---
    print()
    print("=== Демонстрація захисту від порожнього стека ===")
    print("Виштовхуємо всі елементи зі стека:")
    while not stack.is_empty():
        print(f"  pop -> {stack.pop()}")
 
    print("Спроба pop з порожнього стека:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"  Виняток перехоплено: {e}")
 
 
if __name__ == "__main__":
    main()
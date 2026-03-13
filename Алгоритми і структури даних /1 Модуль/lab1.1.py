from VectorList import VectorList
from LinkedStack import LinkedStack
from Node import Node

my_list = VectorList(10)
my_stack = LinkedStack()

# 2. Заповнення списку (Рівень 1)
test_data = ["10", "55", "42", "61", "125", "7", "50", "99"]
for val in test_data:
    my_list.insert(val)

print("--- Початковий стан ---")
my_list.display()

# 3. Виконання завдання 3-го рівня
print("\n--- Обробка та переміщення ---")
# Оскільки ми "переміщуємо", будемо йти з кінця списку, щоб видалення не псувало індекси
i = 0
while i < my_list.count:
    val_int = int(my_list.items[i])
    
    if val_int > 50 and val_int % 2 != 0:
        print(f"Знайдено {val_int}: переміщуємо у стек.")
        my_stack.push(val_int)
        my_list.remove_at(i)
        # Не збільшуємо i, бо елементи зсунулися
    else:
        i += 1

# 4. Виведення результатів
print("\n--- Кінцевий стан ---")
my_list.display()
my_stack.display()
from menu_list import menu_list
from menu_array import menu_array
from menu_deque import menu_deque
from binary_tree import binary_tree

def main_menu():
    while True:
        print("\n=== Головне меню ===")
        print("1. List")
        print("2. Deque")
        print("3. Array")
        print("4. Дерево")
        print("0. Вихід")
        choice = input("Вибір: ")

        if choice == "1":
            menu_list()
        elif choice == "2":
            menu_deque()
        elif choice == "3":
            menu_array()
        elif choice == "4":
            menu_tree()
        elif choice == "0":
            print("Bye!")
            break

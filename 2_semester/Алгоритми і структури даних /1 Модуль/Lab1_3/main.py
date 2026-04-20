from student import Student
from binarytree import BinaryTree
from binarytree import TreeNode

def main():
    students = [
        Student("Коваленко",  "Андрій",   3, 1050, False), 
        Student("Бондаренко", "Олег",     5, 1030, True),   
        Student("Мельник",    "Іван",     2, 1070, False),  
        Student("Гриценко",   "Василь",   5, 1010, True),   
        Student("Романенко",  "Микола",   4, 1040, True),  
        Student("Петренко",   "Сергій",   5, 1060, True),   
        Student("Шевченко",   "Олексій",  1, 1090, False),  
        Student("Ткаченко",   "Дмитро",   5, 1035, True),  
        Student("Лисенко",    "Юрій",     3, 1020, False),  
        Student("Кравченко",  "Руслан",   2, 1080, False),  
    ]
 
    tree = BinaryTree()
    print("\n  Додавання студентів до дерева:")
    for s in students:
        army = "армія" if s.served_in_army else "     "
        print(f"    + #{s.student_id}  {s.last_name} {s.first_name}"
              f"  курс {s.course}  [{army}]")
        tree.insert(s)
 
    tree.print_tree_visual(title="Дерево ДО видалення (Візуально)")
 
    criterion_nodes: list[Student] = []
    tree._find_by_criteria(tree.root, 5, True, criterion_nodes)
    print("  Вузли, що підпадають під критерій (5-й курс + армія):")
    print(f"  {'Квиток':<10} {'Прізвище':<15} {'Name':<12} {'Курс':<7} Армія")
    print(f"  {'─' * 55}")
    for s in criterion_nodes:
        print(s)
    print()
 
    print("  Виконується видалення...")
    deleted = tree.delete_by_criteria(course=5, served=True)
    print(f"  Видалено вузлів: {deleted}\n")
    print("  Варіанти видалення, що були продемонстровані:")
    print("    1. Лист (без нащадків)              — Гриценко #1010, Петренко #1060")
    print("    2. Один нащадок                     — Ткаченко #1035")
    print("    3. Два нащадки                      — Бондаренко #1030")
    print("    4. Батьківський + дочірній вузли    — #1030 (батько) та #1035 (дочірній)")
 
    tree.print_tree_visual(title="Дерево ПІСЛЯ видалення (Візуально)")
 
 
if __name__ == "__main__":
    main()
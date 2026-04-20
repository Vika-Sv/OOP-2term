from student import Student
from bst import BST

W = 74

STUDENTS_DATA = [
    ("Шевченко",  "Олександр",  15,  3, 2002, "туризм"),
    ("Іваненко",  "Марія",       4,  7, 2001, "малювання"),
    ("Коваленко", "Дмитро",     22, 11, 2003, "спорт"),
    ("Бондаренко","Анна",        8,  1, 2000, "читання"),
    ("Ткаченко",  "Юрій",       30,  6, 2002, "музика"),
    ("Кравченко", "Ірина",      17,  9, 2004, "туризм"),
    ("Олійник",   "Тарас",       3,  2, 1999, "фотографія"),
    ("Мороз",     "Оксана",     25, 12, 2001, "кулінарія"),
    ("Лисенко",   "Андрій",     11,  5, 2003, "шахи"),
    ("Гриценко",  "Наталія",    19,  8, 2000, "туризм"),   # улітку + туризм
    ("Поліщук",   "Михайло",     6, 10, 2002, "туризм"),
    ("Савченко",  "Людмила",    28,  4, 2001, "малювання"),
    ("Бойко",     "Іван",       14,  6, 2000, "спорт"),
    ("Левченко",  "Софія",       2,  3, 2005, "музика"),
    ("Марченко",  "Олена",      20,  1, 2003, "читання"),
    ("Романенко", "Дмитро",      9,  7, 2004, "туризм"),   # улітку + туризм
    ("Захаренко", "Вікторія",   16, 11, 2001, "фотографія"),
    ("Федоренко", "Олексій",    27,  2, 2000, "туризм"),
    ("Мельник",   "Катерина",    5,  9, 2002, "кулінарія"),
    ("Павленко",  "Сергій",     13,  4, 2003, "шахи"),
]

def sequential_search(arr: list[Student], predicate) -> int: 
        count = 0
        for i in range(len(arr)):
            if predicate(arr[i]):
                count += 1
        return -count if count > 0 else 0

def print_array(arr: list[Student], title: str = ""):
    print(f"\n{'─'*W}")
    if title:
        print(f"  {title}")
        print(f"{'─'*W}")
    print(f"  {'№':<4} {'Прізвище':<14} {'Ім\'я':<12} "
          f"{'Дата нар.':<14} Хобі")
    print(f"  {'─'*(W-2)}")
    for i, s in enumerate(arr, 1):
        print(f"  {i:<4} {s}")
    print(f"{'─'*W}")
    print(f"  Кількість елементів: {len(arr)}")


def header(text: str):
    print(f"  {text}")
 
 
def main():
    header("Одновимірний масив, послідовний пошук")

    students = [Student(*d) for d in STUDENTS_DATA]
    print_array(students, "Початковий масив (невпорядкований, 20 елементів)")

    search_result = sequential_search(students, lambda s: s.is_born_in_summer() and s.likes_tourism())
    count_found = -search_result if search_result < 0 else 0
    status = (f"знайдено {count_found} елемент(ів)" if search_result < 0 else "не знайдено (null)")
    print(f"  Результат пошуку: {search_result}  ({status})")
 
    if search_result == 0:
        print("  Студентів за заданою умовою не знайдено.")
        return

    indices_to_delete = [
        i for i, s in enumerate(students)
        if s.is_born_in_summer() and s.likes_tourism()
    ]
    print(f"  Індекси елементів для видалення: {indices_to_delete}")
    for idx in indices_to_delete:
        print(f"    [{idx:>2}]  {students[idx]}")

    for idx in sorted(indices_to_delete, reverse=True):
        students.pop(idx)
 
    print_array(students,f"Масив після видалення ({len(students)} елементів)")

    header("BST-дерево (вставка в корінь + DSW-балансування)")

    bst = BST()
    print("  Додавання вузлів (формат: [ключ] Прізвище дата / хобі):")
 
    for d in STUDENTS_DATA:
        bst.insert(Student(*d))

    bst.print_bfs_full(
        "Фінальний стан BST-дерева (обхід у ширину, детально)"
    )
 
    print(f"\n{'─'*W}")
    print("  Демонстрація ротацій")
    print(f"{'─'*W}")
    print(f"  Корінь до ротації:  [{bst.root.key}] "
          f"{bst.root.student.last_name}")
 
    if bst.root.right:
        bst.root = bst.rotate_left(bst.root)
        print(f"  Після rotate_left:  [{bst.root.key}] " 
              f"{bst.root.student.last_name}")
    if bst.root.left:
        bst.root = bst.rotate_right(bst.root)
        print(f"  Після rotate_right: [{bst.root.key}] "
              f"{bst.root.student.last_name}")

    print(f"\n{'─'*W}")
    print("  Пошук за ключем (дата народження → формат РРРРMMДД)")
    print(f"{'─'*W}")
 
    queries = [
        (20000819, "19.08.2000 — Гриценко Наталія"),
        (19990203, "03.02.1999 — Олійник Тарас"),
        (20011231, "31.12.2001 — не існує"),
    ]
    for key, label in queries:
        print(f"\n  Шукаємо ключ {key}  ({label}):")
        node = bst.search(key)
        if node:
            print(f"      Знайдено: {node.student}")
        else:
            print("      Результат: None")


if __name__ == "__main__":
    main()
from student import Student  
import random

def heapify(arr: list[Student], n: int, root: int) -> None:
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < n and arr[left].group > arr[largest].group:
        largest = left

    if right < n and arr[right].group > arr[largest].group:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, n, largest)


def heap_sort(arr: list[Student]) -> None:
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  
        heapify(arr, i, 0)           


def print_students(students: list[Student], title: str) -> None:
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")
    for s in students:
        print(s)
    print(f"{'=' * 50}")


students = [
    Student("Коваленко", "Олена",  124, "ФКНТ"),
    Student("Мельник",   "Іван",   54, "ФПКП"),
    Student("Бойко",     "Анна",   152, "ФАЕТ"),
    Student("Ткач",      "Сергій", 122, "ФКНТ"),
    Student("Гнатенко",  "Марія",  173, "АКФ"),
    Student("Савченко",  "Петро",  312, "ФПКП"),
    Student("Лисенко",   "Юлія",   121, "ФКНТ"),
]

# ── Вивід до сортування ───────────────────────────
print_students(students, "ДО СОРТУВАННЯ")

# ── Сортування ────────────────────────────────────
heap_sort(students)

# ── Вивід після сортування ────────────────────────
print_students(students, "ПІСЛЯ СОРТУВАННЯ (за зростанням групи)")

from student import Student  

def heapify_by_group(arr, n, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < n and arr[left].group > arr[largest].group:
        largest = left
    if right < n and arr[right].group > arr[largest].group:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify_by_group

def heap_sort_by_group(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_by_group(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_by_group(arr, i, 0)

def index_sort_by_surname(arr, start, end):
    size = end - start
    indices = list(range(start, end))
    for i in range(1, size):
        key_idx = indices[i]
        j = i - 1
        while j >= 0 and arr[indices[j]].surname > arr[key_idx].surname:
            indices[j + 1] = indices[j]
            j -= 1
        indices[j + 1] = key_idx

    sorted_block = [arr[i] for i in indices]
    for i in range(size):
        arr[start + i] = sorted_block[i]

def sort_within_groups_by_surname_index(arr):
    i = 0
    while i < len(arr):
        j = i
        while j < len(arr) and arr[j].group == arr[i].group:
            j += 1
        if j - i > 1:
            index_sort_by_surname(arr, i, j)  
        i = j

def print_students(students: list['Student'], title: str) -> None:
    print(f"{title}:")
    for s in students:
        print(s)



students = [
    Student("Коваленко", "Олена",  121, "ФКНТ"),
    Student("Мельник", "Іван",   54, "ФПКП"),
    Student("Бойко", "Анна",   152, "ФАЕТ"),
    Student("Бондаренко","Сергій", 121, "ФКНТ"),
    Student("Гнатенко", "Марія",  173, "АКФ"),
    Student("Савченко", "Петро",  312, "ФПКП"),
    Student("Лисенко", "Юлія",   121, "ФКНТ"),
]


print_students(students, "ДО СОРТУВАННЯ")

heap_sort_by_group(students)
sort_within_groups_by_surname_index(students)

print()  

print_students(students, "ПІСЛЯ СОРТУВАННЯ")

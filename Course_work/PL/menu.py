from BLL.exceptions import ValidationError, NotFoundError, CapacityError
from BLL.student_service import StudentService
from BLL.group_service import GroupService
from BLL.dorm_service import DormService



class Menu:
    def __init__(self, student_service, group_service, dorm_service):
        self.student_service = student_service
        self.group_service = group_service
        self.dorm_service = dorm_service

    def run(self):
        while True:
            print('\n===== ГОЛОВНЕ МЕНЮ =====')
            print('1. Студенти')
            print('2. Групи')
            print('3. Гуртожиток')
            print('4. Пошук')
            print('0. Вихід')

            ch = input('Ваш вибір: ')

            if ch == '1': self.menu_students()
            elif ch == '2': self.menu_group()
            elif ch == '3': self.menu_dorm()
            elif ch == '4': self.menu_search()
            elif ch == '0': break
            else:
                print('Невірний вибір!')

   
    def menu_students(self):
        print('\n--- Студенти ---')
        print('1.1 Додати')
        print('1.2 Видалити')
        print('1.3 Змінити')
        print('1.4 Переглянути всіх')
        print('1.5 Переглянути одного')
        print('0. Назад')

        c = input('Ваш вибір: ')

        if c == '1': self.add_student()
        elif c == '2': self.delete_student()
        elif c == '3': self.update_student()
        elif c == '4': self.show_all_students()
        elif c == '5': self.show_one_student()

    def add_student(self):
        name = input('Імʼя: ')
        surname = input('Прізвище: ')
        sid = input('ID: ')
        gender = input('Стать (M/F): ')
        address = input('Адреса: ')
        self.student_service.add_student(name, surname, sid, gender, address)
        print('Студнт був доданий')

    def delete_student(self):
        sid = input('ID студента: ')
        self.student_service.delete_student(sid)
        print('Студнт був видалний')

    def update_student(self):
        sid = input('ID студента: ')
        name = input('Нове імʼя: ')
        surname = input('Нове прізвище: ')
        gender = input('Стать (M/F): ')
        address = input('Адреса: ')
        group_id = input('ID групи: ')

        self.student_service.update_student(
            sid,
            name or None,
            surname or None,
            gender or None,
            address or None,
            group_id or None
        )
        print('Студента була оновлено')

    def show_all_students(self):
        all_st = self.student_service.students.get_all()

        if not all_st:
            print('Студентів поки немає')
            return

        for s in all_st:
            print(s)


    def show_one_student(self):
        sid = input('ID студента: ')
        print(self.student_service.get_by_id(sid))

   
    def menu_group(self):
        print('\n--- Групи ---')
        print('2.1 Додати групу')
        print('2.2 Видалити групу')
        print('2.3 Змінити групу')
        print('2.4 Переглянути всі групи')
        print('2.5 Переглянути одну групу')
        print('2.6 Додати студента у групу')
        print('2.7 Видалити студента з групи')
        print('0. Назад')

        c = input('Ваш вибір: ')

        if c == '1': self.add_group()
        elif c == '2': self.delete_group()
        elif c == '3': self.update_group()
        elif c == '4': self.show_all_groups()
        elif c == '5': self.show_one_group()
        elif c == '6': self.add_student_to_group()
        elif c == '7': self.remove_student_from_group()

    def add_group(self):
        degree = input('Ступінь: ')
        major = input('Спеціальність: ')
        year = input('Рік: ')
        course = input('Курс: ')
        ep = input('Освітня програма: ')
        self.group_service.add_group(degree, major, year, course, ep)
        print('Грпу було створено')

    def delete_group(self):
        course = input('Номер групи: ')
        self.group_service.delete_group(course)
        print('Групу було видалено')

    def update_group(self):
        course = input('Номер групи: ')
        degree = input('Новий ступінь: ')
        major = input('Нова спеціальність: ')
        year = input('Новий курс: ')
        ep = input('Освітня програма: ')
        self.group_service.update_group(course, degree or None, major or None, year or None, ep or None)
        print('Групу було оновлено')

    def show_all_groups(self):
        all_gr = self.group_service.groups.get_all()

        if not all_gr:
            print('Група порожня')
            return
        
        for i in all_gr:
            print(i)

    def show_one_group(self):
        gmaj = input('Спеціальність: ')
        gyear = input('Рік вступу: ')
        print(self.group_service.get_group(gmaj, gyear))

    def add_student_to_group(self):
        full_group_text = input('Введіть повний запис групи (наприклад Б-121-24-1-ПІ): ')
        sid = input('ID студента: ')

    
        target_group = None
        for g in self.group_service.groups.get_all():
            if str(g) == full_group_text:
                target_group = g
                break

        if not target_group:
            print('Групу не знайдено!')
            return

   
        self.group_service.add_student_to_group(target_group, sid)
        print('Студента було додано до групи')

    def remove_student_from_group(self):
        course = input('ID групи: ')
        sid = input('ID студента: ')
        self.group_service.remove_student_from_group(course, sid)
        print('Студент був видалений з групи')

    
    def menu_dorm(self):
        print('\n--- Гуртожиток ---')
        print('3.1 Додати кімнату')
        print('3.2 Змінити кімнату')
        print('3.3 Поселити студента')
        print('3.4 Виписати студента')
        print('3.5 Переглянути всі кімнати')
        print('0. Назад')

        c = input('Ваш вибір: ')

        if c == '1': self.add_room()
        elif c == '2': self.update_room()
        elif c == '3': self.check_in()
        elif c == '4': self.check_out()
        elif c == '5': self.show_rooms()

    def add_room(self):
        dorm = input('Dorm number: ')
        room = input('Номер кімнати: ')
        cap = input('Місткість: ')
        
        if not cap.isdigit():
            print('Помилка: місткість повинна бути числом.')
            return

        cap = int(cap)

        self.dorm_service.add_room(dorm, room, cap)
        print('Кімнату успішно додано!')

    def update_room(self):
        dorm = input('Dorm number: ')
        room = input('Номер кімнати: ')
        cap = input('Нова місткість: ')
        self.dorm_service.update_room(num, int(cap) if cap else None)
        print('Кімната була оновлена')

    def check_in(self):
        dorm = input('Номер гуртожитку: ')
        room = input('Номер кімнати: ')
        sid = input('ID студента: ')

        try:
            self.dorm_service.check_in(dorm, room, sid)
            print('Студента поселено!')
        except Exception as e:
            print(e)


    def check_out(self):
        dorm = input('Номер гуртожитку: ')
        room = input('Номер кімнати: ')
        sid = input('ID студента: ')

        try:
            self.dorm_service.check_out(dorm, room, sid)
            print('Студента виписано!')
        except Exception as e:
            print(e)


    def show_rooms(self):
        all_dr = self.dorm_service.get_all_rooms()

        if not all_dr:
            print('Ніхто поки що не живе тут')
            return
        
        for r in all_dr:
            print(r)

 
    def menu_search(self):
        print('\n--- Пошук ---')
        print('4.1 Студент за імʼям та прізвищем')
        print('4.2 Студенти за повним записом групи')
        print('4.3 Студенти у гуртожитку')
        print('0. Назад')

        c = input('Ваш вибір: ')

        if c == '1': 
            self.search_by_name()
        elif c == '2': 
            self.search_group_students()
        elif c == '3': 
            self.search_dorm_students()

   
    def search_by_name(self):
        name = input('Імʼя: ')
        surname = input('Прізвище: ')

        results = self.student_service.find_by_name(name, surname)

        if not results:
            print('Студента не знайдено.')
            return

        for st in results:
            print(st)

    
    def search_group_students(self):
        full_group_text = input('Введіть повний формат групи: ')


        group_obj = self.group_service.groups.find(
        lambda g: str(g) == full_group_text
        )

        if not group_obj:
            print('Групу не знайдено!')
            return

        students = self.student_service.students.find_all(
        lambda s: s.student_id in group_obj.students
        )

        if not students:
            print('У цій групі немає студентів.')
            return

        for st in students:
            print(st)

   
    def search_dorm_students(self):
        rooms = self.dorm_service.get_all_rooms()

        if not rooms:
            print('Немає жодної кімнати.')
            return

        for room in rooms:
            for sid in room.students:

                student = self.student_service.students.find(
                    lambda s: s.student_id == sid
                )

                if student:
                    print(f'Гуртожиток {room.dorm_number}, кімната {room.room_number}: {student}')

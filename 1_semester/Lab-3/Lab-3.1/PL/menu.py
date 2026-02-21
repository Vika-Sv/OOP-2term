from clases.student import Student

class Menu:
    def __init__(self, service):
        self.service = service

    def main_menu(self):
        while True:
            print('\n STUDENT MENU')
            print('1. Add sudent')
            print('2. Show all student')
            print('3. Count students (M, 3 course, dorm)')
            print('4. Save in file')
            print('0. Exit')

            choice = input('Your choice: ')

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.show_all()
            elif choice == '3':
                print('Result:', self.service.count_male_third_course_in_dorm())
            elif choice == '4':
                self.service.save()
                print('Data saved')
            elif choice == '0':
                break
            else:
                print('Wrong choice!')

    def add_student(self):
        fn = input('Name: ')
        ln = input('Surname: ')
        course = int(input('Course: '))
        sid = input('ID (AA №00000000): ')
        gender = input('Gender (M/F): ')
        adr = input('Adress: ')
        s = Student(fn, ln, course, sid, gender, adr)
        self.service.add_student(s)

    def show_all(self):
        students = self.service.get_all_students()
        if not students:
            print('List is empty')
        else:
            for s in students:
                print(s.info())
                s.SleepStanding()

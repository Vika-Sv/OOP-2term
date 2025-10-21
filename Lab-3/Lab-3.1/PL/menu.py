import re  
from DAL.entity.student import Student
from BLL.entity_service import EntityService
from DAL.entity_context import EntityContext
from BLL.exceptions import StudentException



class Menu:
    def __init__(self):
        self.service = EntityService(EntityContext())
        self.persons = []  
        self.db = EntityContext() 

    def add_student(self):
        fn = input('Enter first name: ')
        ln = input('Enter last name: ')
        g = input('Enter gender (M/F): ')
        
        if not re.match(r'^[MF]$', g, re.IGNORECASE):
            print('Wrong format')
            return
        
        c = int(input('Enter course: '))
        a = input('Enter address (e.g. 12-34 if dorm): ')
        sid = input('Enter ID (AA №00000000): ')
        
        if not re.match(r'^[A-Z]{2} №\d{8}$', sid):
            print('Wrong format')
            return
        
        s = Student(last_name=ln, first_name=fn, gender=g.upper(), course=c, dorm=a, student_id=sid)
        self.persons.append(s)
        print('Student is added')

    def show_all(self):
        if not self.persons:
            print('None')
        else:
            for p in self.persons:
                print(p)

    def save_to_file(self):
        self.db.save(self.persons)
        print('Data saved')

    def load_from_file(self):
        data = self.db.load()
        print('Downloaded from file: ')
        for line in data:
            print(line)

    def count_students(self):
        count = 0
        for s in self.persons:
            if s.course == 2 and s.gender.upper() == 'M' and re.match(r"^\d+-\d+$", str(s.dorm)):
                count += 1
        print(f'Result: {count}')

    def main_menu(self):
        while True:
            print('\n--- Menu ---')
            print('1. Add student')
            print('2. Show all')
            print('3. Save in file')
            print('4. Download from file')
            print('5. Count the Students (M, 2 course, dorm)')
            print('0. Exit')
            choice = input('Your choice: ')

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.show_all()
            elif choice == '3':
                self.save_to_file()
            elif choice == '4':
                self.load_from_file()
            elif choice == '5':
                self.count_students()
            elif choice == '0':
                break    
            else:
                print('Wrong choice!')

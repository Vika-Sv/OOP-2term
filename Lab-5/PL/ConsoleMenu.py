import re
from BLL.student import Student 
from BLL.student_logic import StudentLogic

class ConsoleMenu:
    def __init__(self, logic: StudentLogic):
        self.logic = logic
    
    def AddStudent(self):
        try:
            Fn = input('Enter first name: ')
            Ln = input('Enter last name: ')
            G = input('Enter gender (M/F): ').upper()
            
            if not re.match(r'M|f',FG):
                print('Wrong format for Gender')
                return
            
            C = int(input('Enter course: '))
            A = input('Enter adress: ')
            Sid = input('Enter ID (AA №00000000): ')
            
            if not re.match(r'^[A-Z]{2} №\d{8}$', Sid):
                print('Wrong format for Student ID.')
                return
            
            s = Student(FirstName=Fn, LastName=Ln, Gender=G, Course=C, Adress=A, StudentID=Sid)
            self.logic.add_student(s)
            print('Student is added')
            
        except ValueError:
            print('Course must be a number.')
        
    def ShowAll(self):
        persons = self.logic.get_all_students()
        if not persons:
            print('None')
        else:
            for p in persons:
                print(p.info())
                
    def SaveToFile(self):
        self.logic.save_to_file()
        print('Data saved')

    def LoadFromFile(self):
        data = self.logic.load_from_file()
        print('Downloaded from file: ')
        for line in data:
            print(line.strip())
            
    def CountStudents(self):
        count = self.logic.count_third_course_male_dorm_students()
        print(f'Result: {count}')
        
    def menu(self):
        while True:
            print('1. Add student')
            print('2. Show all')
            print('3. Save in file')
            print('4. Download from file')
            print('5. Count the Students (M, 3 course, dorm) - BLL')
            print('0. Exit')
            choice = input('Your choice: ')

            if choice == '1':
                self.AddStudent()
            elif choice == '2':
                self.ShowAll()
            elif choice == '3':
                self.SaveToFile()
            elif choice == '4':
                self.LoadFromFile()
            elif choice == '5':
                self.CountStudents()
            elif choice == '0':
                break
            else:
                print('Wrong choice!')

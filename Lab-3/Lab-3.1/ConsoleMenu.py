import re  
from student import Student 


class ConsoleMenu:
     def __init__(self, db):
        self.db = db
        self.persons = []
    
    
     def AddStudent(self):
        Fn = input('Enter first name: ')
        Ln = input('Enter last name: ')
        G = input('Enter gender: ')
        
        if not re.match(r'M|F', G):
            print('Wrong format')
            return
        
        C = int(input('Enter course: '))
        A = input('Enter adress: ')
        Sid = input('Enter ID (AA №00000000): ')
        
        if not re.match(r'^[A-Z]{2} №\d{8}$', Sid):
            print('Wrong format')
            return
        
        
        s = Student(FirstName=Fn, LastName=Ln, Gender=G, Course=C, Adress=A, StudentID=Sid)
        self.persons.append(s)
        print('Student is added')
        
        
     def ShowAll(self):
         if not self.persons:
            print('None')
         else:
             for p in self.persons:
              print(p.info())


     def SaveToFile(self):
        self.db.save(self.persons)
        print('Data saved')


     def LoadFromFile(self):
        data = self.db.load()
        print('Downloaded from file: ')
        
        for line in data:
            print(line.strip())
           
            
     def CountStudents(self):
         count = 0
         for s in self.persons:
             if s.Course == 2 and s.Gender.upper() == 'M' and re.match(r"^\d+-\d+$", s.Adress):
                 count += 1
         print(f'Result: {count}')
          
     
     def menu(self):
        while True:
            print('1. Add student')
            print('2. Show all')
            print('3. Save in file')
            print('4. Download from file')
            print('5. Count the Students (M, 2 course, dorm)')
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
        
    
        
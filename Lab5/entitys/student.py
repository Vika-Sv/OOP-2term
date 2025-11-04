from entitys.person import Person
import re

class Student(Person):
    def __init__(self, FirstName, LastName, Course, StudentID, Gender, Adress):
        super().__init__(FirstName, LastName)
        self.Course = Course
        self.StudentID = StudentID
        self.Gender = Gender
        self.Adress = Adress
    
    def info(self):
        return f'Student: {self.FirstName} {self.LastName}, Course: {self.Course}, ID: {self.StudentID}, Gender: {self.Gender}, Adress: {self.Adress}'
        
    def is_dormitory_resident(self):
        return bool(re.match(r"^\d+-\d+$", str(self.Adress)))    
    
    
    def SleepStanding(self):
        return f'{self.FirstName} {self.LastName} can sleep while standing.'

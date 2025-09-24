from person import Person

class Student(Person):
    def __init__(self, FirstName, LastName, Course, StudentID, Gender, Adress):
        super().__init__(FirstName, LastName)
        self.Course = Course
        self.StudentID = StudentID
        self.Gender = Gender
        self.Adress = Adress
    
    def info(self):
        return f'Student: {self.FirstName}{self.LastName}, Course{self.Course}, ID: {self.StudentID}, Gender: {self.Gender}, Adress: {self.Adress}'
        
    def SleepStnding(self):
        print(f'{self.FirstName} {LastName} can sleep while standing.')     
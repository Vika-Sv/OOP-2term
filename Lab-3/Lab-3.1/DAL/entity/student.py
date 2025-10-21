from DAL.entity.person import Person

class Student(Person):
    def __init__(self, first_name, last_name, gender, course, student_id, dorm=None):
        super().__init__(first_name, last_name, gender)
        self.course = course
        self.student_id = student_id
        self.dorm = dorm

    def info(self):
        return (f"Student: {self.first_name} {self.last_name}, "
                f"Course: {self.course}, ID: {self.student_id}, "
                f"Gender: {self.gender}, Dorm: {self.dorm}")

    def __str__(self):  
        return self.info()

    def sleep_standing(self):
        print(f"{self.first_name} {self.last_name} can sleep while standing.")

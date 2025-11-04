from BLL.exceptions import StudentNotFoundException

class EntityService:
    def __init__(self, context):
        self.context = context
        self.students = context.load()

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return self.students

    def count_male_third_course_in_dorm(self):
        count = 0
        for s in self.students:
            if s.Course == 3 and s.Gender.upper() == 'M' and '-' in s.Adress:
                count += 1
        return count

    def save(self):
        self.context.save(self.students)

    def find_student(self, student_id):
        for s in self.students:
            if s.StudentID == student_id:
                return s
        raise StudentNotFoundException(f'Student with ID {student_id} not found')

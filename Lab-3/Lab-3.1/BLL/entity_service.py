from BLL.exceptions import StudentException

class EntityService:
    def __init__(self, context):
        self.context = context

    def add_student(self, student):
        students = self.context.load()
        students.append(student)
        self.context.save(students)

    def get_all(self):
        return self.context.load()

    def count_male_third_course_in_dorm(self):
        students = self.context.load()
        count = sum(1 for s in students if s.course == 3 and s.gender == "M" and s.dorm is not None)
        if count == 0:
            raise StudentException('This student don\'t exist')
        return count

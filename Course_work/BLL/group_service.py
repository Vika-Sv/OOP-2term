from BLL.exceptions import NotFoundError, ValidationError
from BLL.group import Group
from BLL.generic_collection import Generic

class GroupService:
    def __init__(self, groups):
        self.groups = groups

    def add_group(self, degree, major, year, course, educational_program):
        if self.groups.find(lambda g: g.course == course):
            raise ValidationError("Група вже існує.")

        g = Group(degree, major, year, course, educational_program)
        self.groups.add(g)
        return g

   
    def delete_group(self, course):
        g = self.groups.find(lambda x: x.course == course)
        if not g:
            raise NotFoundError("Групу не знайдено.")
        self.groups.remove(g)

   
    def update_group(self, course, degree=None, major=None, year=None, educational_program=None):
        g = self.groups.find(lambda x: x.course == course)
        if not g:
            raise NotFoundError("Групу не знайдено.")

        if degree: g.degree = degree
        if major: g.major = major
        if year: g.year = year
        if educational_program: g.educational_program = educational_program

        return g

    
    def get_group(self, major, year):
        g = self.groups.find(lambda x: x.major == major and x.year == year)
        if not g:
            raise NotFoundError("Групу не знайдено.")
            return g

    
    def add_student_to_group(self, group: Group, student_id: str):
        if student_id in group.students:
            raise ValidationError("Студент уже в цій групі.")

        group.add_student(student_id)
        return group


    
    def remove_student_from_group(self, course, student_id):
        g = self.groups.find(lambda x: x.course == course)
        if not g:
            raise NotFoundError("Групу не знайдено.")

        g.remove_student(student_id)
        return g

    
    def get_students_in_group(self, course, student_collection):
        group = self.groups.find(lambda g: g.course == course)
        if not group:
            raise NotFoundError("Групу не знайдено.")

        students = student_collection.find_all(lambda s: s.course == course)
        return students

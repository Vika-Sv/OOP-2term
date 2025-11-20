from BLL.exceptions import NotFoundError, ValidationError
from DAL.enteties.student import Student
from BLL.generic_collection import Collection


class StudentService:
    def __init__(self, students: Collection[Student]):
        self.students = students

    def add_student(self, name, surname, student_id, gender, address=None):
        if gender not in ('M', 'F'):
            raise ValidationError('Стать повинна бути ''M'' або 'F'.')

        if self.students.find(lambda s: s.student_id == student_id):
            raise ValidationError('Студент з таким ID вже існує.')

        st = Student(name, surname, student_id, gender, address)
        self.students.add(st)
        return st

    def delete_student(self, student_id):
        student = self.students.find(lambda s: s.student_id == student_id)
        if not student:
            raise NotFoundError("Студента не знайдено.")

        self.students.remove(student)
        return student

    def update_student(self, student_id, name=None, surname=None, gender=None, address=None):
        st = self.students.find(lambda s: s.student_id == student_id)
        if not st:
            raise NotFoundError('Студента не знайдено.')

        if name:
            st.name = name
        if surname:
            st.surname = surname

        gender = gender.strip().upper()
        if gender:
            if gender not in ('M', 'F'):
                raise ValidationError('Стать повинна бути ''M'' або 'F'.')
            st.gender = gender

        if address:
            st.address = address

        return st

    def get_by_id(self, student_id):
        st = self.students.find(lambda s: s.student_id == student_id)
        if not st:
            raise NotFoundError('Студента не знайдено.')
        return st

    def get_all(self):
        return self.students.get_all()
    
    def find_by_name(self, name, surname):
        res = []
        for st in self.students.get_all():
            if st.name.lower() == name.lower() and st.surname.lower() == surname.lower():
                res.append(st)

        if not res:
            raise NotFoundError('Студентів з такими даними не знайдено.')
        return res



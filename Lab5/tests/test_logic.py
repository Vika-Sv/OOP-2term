import pytest
from entitys.student import Student
from BLL.student_logic import StudentLogic

class FakeRepository:
    def __init__(self):
        self.saved_data = None

    def save(self, students):
        self.saved_data = students

    def load(self):
        return ['line1', 'line2']

def make_student(LastName='Test', FirstName='Student', Course=1, Gender='M', Dorm='1-101'):
    return Student(
        FirstName=FirstName,
        LastName=LastName,
        Course=Course,
        StudentID='AA №12345678',
        Gender=Gender,
        Adress=Dorm
    )

def test_add_and_get_students():
    repo = FakeRepository()
    logic = StudentLogic(repo)
    student = make_student()
    logic.add_student(student)

    students = logic.get_all_students()
    
    assert len(students) == 1
    assert students[0].FirstName == 'Student'

def test_save_to_file_saves_students():
    repo = FakeRepository()
    logic = StudentLogic(repo)
    student = make_student()
    logic.add_student(student)

    logic.save_to_file()
    assert repo.saved_data is not None
    assert len(repo.saved_data) == 1
    assert repo.saved_data[0].LastName == 'Test'

def test_load_from_file_returns_lines():
    repo = FakeRepository()
    logic = StudentLogic(repo)
    lines = logic.load_from_file()
    assert lines == ['line1', 'line2']

def test_count_third_course_male_dorm_students():
    repo = FakeRepository()
    logic = StudentLogic(repo)
    s1 = make_student(Course=3, Gender='M', Dorm='5-201')   # valid
    s2 = make_student(Course=3, Gender='F', Dorm='5-202')   # invalid
    s3 = make_student(Course=2, Gender='M', Dorm='5-203')   # invalid
    s4 = make_student(Course=3, Gender='M', Dorm='Kyiv')    # invalid

    logic.add_student(s1)
    logic.add_student(s2)
    logic.add_student(s3)
    logic.add_student(s4)

    result = logic.count_third_course_male_dorm_students()
    assert result == 1

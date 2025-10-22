import pytest
from BLL.student import Student 
from BLL.student_logic import StudentLogic

class MockRepository:
    def save(self, data):
        self.saved_data = data
    def load(self):
        return ["mocked line 1", "mocked line 2"]

@pytest.fixture
def student_logic():
    mock_repo = MockRepository()
    return StudentLogic(mock_repo)

@pytest.fixture
def test_students_for_count():
    return [
        Student('Іван', 'Коваленко', 3, 'ID1', 'M', '2-105'),   
        Student('Олена', 'Петрова', 2, 'ID2', 'M', '3-200'),    
        Student('Марія', 'Сидоренко', 3, 'ID3', 'F', '1-300'),  
        Student('Олег', 'Іванов', 3, 'ID4', 'M', 'вул. Шевченка 10'),
        Student('Петро', 'Мельник', 3, 'ID5', 'M', '5-501'),    
    ]

class TestStudentLogic:
    def test_count_third_course_male_dorm_students(self, student_logic, test_students_for_count):
        for student in test_students_for_count:
            student_logic.add_student(student)
        count = student_logic.count_third_course_male_dorm_students() 
        assert count == 2

    def test_add_and_get_students(self, student_logic):
        test_student = Student('Тест', 'Студент', 1, 'IDT', 'M', '1-1')
        student_logic.add_student(test_student)
        students = student_logic.get_all_students()
        assert len(students) == 1
        assert students[0].FirstName == 'Тест'
        assert students[0].LastName == 'Студент'
        
    def test_save_data_delegation(self, student_logic):
        student = Student('Test', 'Save', 1, 'IDS', 'M', '1-2')
        student_logic.add_student(student)
        student_logic.save_to_file()
        assert hasattr(student_logic._repository, "saved_data")
        assert len(student_logic._repository.saved_data) == 1
        assert student_logic._repository.saved_data[0].FirstName == 'Test'

    def test_load_data_delegation(self, student_logic):
        data = student_logic.load_from_file()
        assert isinstance(data, list)
        assert "mocked line 1" in data

import pytest
from BLL.person import Person 
from BLL.student import Student 

@pytest.fixture
def sample_student_dorm():
    return Student('Іван', 'Петренко', 3, 'ST1001', 'M', '1-105')

def test_person_is_abstract():
    with pytest.raises(TypeError):
        Person('Abstract', 'Test')

def test_student_initialization_and_inheritance(sample_student_dorm):
    assert sample_student_dorm.FirstName == 'Іван'
    assert sample_student_dorm.LastName == 'Петренко'
    assert sample_student_dorm.Course == 3
    assert sample_student_dorm.StudentID == 'ST1001'

def test_student_info_method_output(sample_student_dorm):
    expected_info = 'Student: Іван Петренко, Course: 3, ID: ST1001, Gender: M, Adress: 1-105'
    actual_info = sample_student_dorm.info()
    assert actual_info == expected_info

def test_student_sleep_standing_ability(sample_student_dorm):
    expected_output = 'Іван Петренко can sleep while standing.'
    actual_output = sample_student_dorm.SleepStanding()
    assert actual_output == expected_output

@pytest.mark.parametrize('address, expected_result', [
    ('2-105', True), 
    ('Київ', False),       
    ('10-abc', False),    
])
def test_student_is_dormitory_resident_logic(address, expected_result):
    student = Student('Test', 'Address', 1, 'ID', 'M', address)
    is_dorm = student.is_dormitory_resident()
    assert is_dorm == expected_result

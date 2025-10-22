from typing import List
from .student import Student 

class StudentLogic:
    def __init__(self, repository):
        self._repository = repository
        self._students: List[Student] = [] 

    def add_student(self, student: Student):
        self._students.append(student)

    def get_all_students(self) -> List[Student]:
        return self._students
    
    def save_to_file(self):
        self._repository.save(self._students)
        
    def load_from_file(self) -> List[str]:
        raw_lines = self._repository.load()
        return raw_lines 

    def count_third_course_male_dorm_students(self) -> int:
        count = 0
        for s in self._students:
            is_male = s.Gender.upper() == 'M'
            is_third_course = s.Course == 3
            is_dorm_resident = s.is_dormitory_resident()
            
            if is_male and is_third_course and is_dorm_resident:
                count += 1
        return count

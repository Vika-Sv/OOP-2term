import json
from pathlib import Path
from DAL.enteties.student import Student

class StudentData:
    def __init__(self, filename='DAL/data/students.json'):
        self.file = Path(filename)
        self.file.parent.mkdir(parents=True, exist_ok=True)

    def load_all(self):
        if not self.file.exists():
            return []

        with self.file.open('r', encoding='utf-8') as f:
            raw = json.load(f)

        students = []
        for d in raw:
            students.append(
                Student(
                    name=d['name'],
                    surname=d['surname'],
                    student_id=d['student_id'],
                    gender=d['gender'],
                    address=d.get('address')
                )
            )
        return students

    def save_all(self, students):
        raw = []

        for s in students:
            raw.append({
                'name': s.name,
                'surname': s.surname,
                'student_id': s.student_id,
                'gender': s.gender,
                'address': s.address,
            })

        with self.file.open('w', encoding='utf-8') as f:
            json.dump(raw, f, ensure_ascii=False, indent=4)

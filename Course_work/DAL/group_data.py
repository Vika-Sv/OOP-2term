import json
from pathlib import Path
from DAL.enteties.group import Group

class GroupData:
    def __init__(self, filename='DAL/data/groups.json'):
        self.file = Path(filename)
        self.file.parent.mkdir(parents=True, exist_ok=True)

    def load_all(self):
        if not self.file.exists():
            return []

        with self.file.open('r', encoding='utf-8') as f:
            raw = json.load(f)

        groups = []

        for d in raw:
            g = Group(
                degree=d['degree'],
                major=d['major'],
                year=d['year'],
                course=d['course'],
                educational_program=d['educational_program']
            )

            for st_id in d.get('students', []):
                g.add_student(st_id)

            groups.append(g)

        return groups

    def save_all(self, groups):
        raw = []

        for g in groups:
            raw.append({
                'degree': g.degree,
                'major': g.major,
                'year': g.year,
                'course': g.course,
                'educational_program': g.educational_program,
                'students': g.students
            })

        with self.file.open('w', encoding='utf-8') as f:
            json.dump(raw, f, ensure_ascii=False, indent=4)

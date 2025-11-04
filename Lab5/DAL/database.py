import json

class Database:
    def __init__(self, filename='database.json'):
        self.filename = filename

    def save(self, persons):
        data = []
        for s in persons:
            data.append({
                'Firstname': s.FirstName,
                'Lastname': s.LastName,
                'StudentId': s.StudentID,
                'Course': s.Course,
                'Gender': s.Gender,
                'Adress': s.Adress
            })
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return []

import json
from clases.student import Student
from abstraction import Abstraction 

class EntityContext(Abstraction):
    def __init__(self, filename="students.json"):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([obj.__dict__ for obj in data], f, ensure_ascii=False, indent=4)

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                raw = json.load(f)
                return [Student(**item) for item in raw]
        except FileNotFoundError:
            return []

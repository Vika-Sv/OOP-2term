import os
from DAL.data_provider import JSONProvider

class EntityContext:
    def __init__(self, filename="students.json"):
        self.filename = filename

    def save(self, students):
        JSONProvider.serialize(students, self.filename)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        return JSONProvider.deserialize(self.filename)

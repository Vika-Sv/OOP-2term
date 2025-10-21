import json
from DAL.entity.student import Student
from DAL.entity.seller import Seller
from DAL.entity.gardener import Gardener

class JSONProvider:
    @staticmethod
    def serialize(students, filename):
        data = []
        for s in students:
            obj = s.__dict__.copy()
            data.append(obj)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def deserialize(filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

            students = []
            for obj in data:
                cls_name = obj.pop("__class__", "Student")
                if cls_name == "Seller":
                    students.append(Seller(**obj))
                elif cls_name == "Gardener":
                    students.append(Gardener(**obj))
                else:
                    students.append(Student(**obj))
            return students

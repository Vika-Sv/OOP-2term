from BLL.person import Person

class Student(Person):
    def __init__(self, name, surname, student_id, gender, address=None):
        super().__init__(name, surname)
        self._student_id = student_id
        self._gender = gender
        self._address = address


    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value

  
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

  
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value


    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "surname": self.surname,
            "student_id": self.student_id,
            "gender": self.gender,
            "address": self.address,
        }

    @staticmethod
    def from_dict(d: dict) -> "Student":
        return Student(
            name=d["name"],
            surname=d["surname"],
            student_id=d["student_id"],
            gender=d["gender"],
            address=d.get("address", ""),
        )

    def __str__(self):
        address = self._address if self._address else 'no address'
        return f'{self.name} {self.surname} ({self._student_id}), {self._gender}, {address}'

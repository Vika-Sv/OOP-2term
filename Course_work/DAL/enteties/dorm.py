class DormRoom:
    def __init__(self, dorm_number, room_number, max_capacity):
        self._dorm_number = dorm_number
        self._room_number = room_number
        self._max_capacity = max_capacity
        self._students = []  

    
    @property
    def dorm_number(self):
        return self._dorm_number

    @dorm_number.setter
    def dorm_number(self, value):
        self._dorm_number = value
    
    
    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        self._room_number = value

 
    @property
    def max_capacity(self):
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, value):
        self._max_capacity = value

    
    @property
    def students(self):
        return self._students

    def add_student(self, student_id):
        if student_id not in self._students:
            self._students.append(student_id)

    def remove_student(self, student_id):
        if student_id in self._students:
            self._students.remove(student_id)

    def free_spaces(self):
        return self._max_capacity - len(self._students)
    
    def to_dict(self) -> dict:
        return {
            'dorm_number': self.dorm_number,
            'room_number': self.room_number,
            'max_capacity': self.max_capacity,
            'students': list(self.students),
        }

    @staticmethod
    def from_dict(d: dict) -> 'DormRoom':
        room = DormRoom(
            dorm_number=d['dorm_number'],
            room_number=d['room_number'],
            max_capacity=d['max_capacity'],
        )
        for sid in d.get('students', []):
            room.add_student(sid)
        return room

    def __str__(self):
        return f'{self._dorm_number}-{self._room_number}'

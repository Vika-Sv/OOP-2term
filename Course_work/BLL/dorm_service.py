from BLL.exceptions import NotFoundError, ValidationError, CapacityError
from DAL.enteties.dorm import DormRoom
from BLL.generic_collection import Collection


class DormService:
    def __init__(self, dorm: Collection[DormRoom]):
        self.dorm = dorm

    def get_by_number(self, dorm_number, room_number):
        room = self.dorm.find(lambda r: r.dorm_number == dorm_number and r.room_number == room_number)
        if not room:
            raise NotFoundError('Кімнату не знайдено.')
        return room

    
    def add_room(self, dorm_number, room_number, max_capacity):
        exists = self.dorm.find(lambda r: r.dorm_number == dorm_number and r.room_number == room_number)
        if exists:
            raise ValidationError('Така кімната вже існує.')

        room = DormRoom(dorm_number, room_number, max_capacity)
        self.dorm.add(room)
        return room

    
    def update_room(self, dorm_number, room_number, new_capacity=None):
        room = self.get_by_number(dorm_number, room_number)

        if new_capacity is not None:
            if new_capacity < len(room.students):
                raise CapacityError('Нова місткість менша за кількість студентів.')
            room.max_capacity = new_capacity

        return room

    
    def check_in(self, dorm_number, room_number, student_id):
        room = self.get_by_number(dorm_number, room_number)

        if len(room.students) >= room.max_capacity:
            raise CapacityError('У кімнаті немає місць.')

        room.add_student(student_id)
        return room

    
    def check_out(self, dorm_number, room_number, student_id):
        room = self.get_by_number(dorm_number, room_number)

        if student_id not in room.students:
            raise NotFoundError('Цей студент не проживає в цій кімнаті.')

        room.remove_student(student_id)
        return room

    
    def get_all_rooms(self):
        return self.dorm.get_all()

    
    def free_spaces(self, dorm_number, room_number):
        room = self.get_by_number(dorm_number, room_number)
        return room.free_spaces()
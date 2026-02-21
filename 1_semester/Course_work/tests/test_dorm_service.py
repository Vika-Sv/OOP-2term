import pytest
from BLL.dorm_service import DormService
from DAL.enteties.dorm import DormRoom
from BLL.exceptions import ValidationError, NotFoundError, CapacityError


class StubDormCollection:
    def __init__(self):
        self.items = []

    def add(self, obj):
        self.items.append(obj)

    def get_all(self):
        return list(self.items)

    def remove(self, obj):
        self.items.remove(obj)

    def find(self, predicate):
        for obj in self.items:
            if predicate(obj):
                return obj
        return None


@pytest.fixture
def service():
    return DormService(StubDormCollection())


def test_add_room_success(service):
    dorm = 'Dorm1'
    room = '101'
    cap = 3

    result = service.add_room(dorm, room, cap)

    assert result.room_number == room


def test_add_room_duplicate(service):
    service.add_room('Dorm1', '101', 3)

    with pytest.raises(ValidationError):
        service.add_room('Dorm1', '101', 3)


def test_get_room_success(service):
    service.add_room('D1', '201', 2)

    result = service.get_by_number('D1', '201')

    assert result.max_capacity == 2


def test_get_room_not_found(service):
    with pytest.raises(NotFoundError):
        service.get_by_number('X', '999')


def test_update_room_capacity_success(service):
    service.add_room('D1', '100', 2)

    result = service.update_room('D1', '100', new_capacity=5)

    assert result.max_capacity == 5


def test_update_room_capacity_too_small(service):
    room = service.add_room('D1', '100', 2)
    room.add_student('AA1')

    with pytest.raises(CapacityError):
        service.update_room('D1', '100', new_capacity=0)


def test_settle_student_success(service):
    service.add_room('D1', '200', 2)

    result = service.check_in('D1', '200', 'AA1')

    assert 'AA1' in result.students


def test_settle_student_over_capacity(service):
    room = service.add_room('D1', '300', 1)
    room.add_student('AA1')

    with pytest.raises(CapacityError):
        service.check_in('D1', '300', 'AA2')


def test_expel_student_success(service):
    room = service.add_room('D1', '400', 3)
    room.add_student('AA1')

    result = service.check_out('D1', '400', 'AA1')

    assert 'AA1' not in result.students


def test_expel_student_not_found(service):
    service.add_room('D1', '500', 3)

    with pytest.raises(NotFoundError):
        service.check_out('D1', '500', 'Z1')


def test_free_spaces(service):
    room = service.add_room('DormZ', '777', 3)
    room.add_student('AA1')

    free = service.free_spaces('DormZ', '777')

    assert free == 2


def test_get_all_rooms(service):
    service.add_room('D1', '101', 2)
    service.add_room('D1', '102', 3)

    rooms = service.get_all_rooms()

    assert len(rooms) == 2

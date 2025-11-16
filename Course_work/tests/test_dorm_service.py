import pytest
from BLL.dorm_service import DormService
from BLL.dorm import DormRoom
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
    # Arrange
    dorm = "Dorm1"
    room = "101"
    cap = 3

    # Act
    result = service.add_room(dorm, room, cap)

    # Assert
    assert result.room_number == room


def test_add_room_duplicate(service):
    # Arrange
    service.add_room("Dorm1", "101", 3)

    # Act / Assert
    with pytest.raises(ValidationError):
        service.add_room("Dorm1", "101", 3)


def test_get_room_success(service):
    # Arrange
    service.add_room("D1", "201", 2)

    # Act
    result = service.get_by_number("D1", "201")

    # Assert
    assert result.max_capacity == 2


def test_get_room_not_found(service):
    # Arrange — none

    # Act / Assert
    with pytest.raises(NotFoundError):
        service.get_by_number("X", "999")


def test_update_room_capacity_success(service):
    # Arrange
    service.add_room("D1", "100", 2)

    # Act
    result = service.update_room("D1", "100", new_capacity=5)

    # Assert
    assert result.max_capacity == 5


def test_update_room_capacity_too_small(service):
    # Arrange
    room = service.add_room("D1", "100", 2)
    room.add_student("AA1")

    # Act / Assert
    with pytest.raises(CapacityError):
        service.update_room("D1", "100", new_capacity=0)


def test_settle_student_success(service):
    # Arrange
    service.add_room("D1", "200", 2)

    # Act
    result = service.check_in("D1", "200", "AA1")

    # Assert
    assert "AA1" in result.students


def test_settle_student_over_capacity(service):
    # Arrange
    room = service.add_room("D1", "300", 1)
    room.add_student("AA1")

    # Act / Assert
    with pytest.raises(CapacityError):
        service.check_in("D1", "300", "AA2")


def test_expel_student_success(service):
    # Arrange
    room = service.add_room("D1", "400", 3)
    room.add_student("AA1")

    # Act
    result = service.check_out("D1", "400", "AA1")

    # Assert
    assert "AA1" not in result.students


def test_expel_student_not_found(service):
    # Arrange
    service.add_room("D1", "500", 3)

    # Act / Assert
    with pytest.raises(NotFoundError):
        service.check_out("D1", "500", "Z1")


def test_free_spaces(service):
    # Arrange
    room = service.add_room("DormZ", "777", 3)
    room.add_student("AA1")

    # Act
    free = service.free_spaces("DormZ", "777")

    # Assert
    assert free == 2


def test_get_all_rooms(service):
    # Arrange
    service.add_room("D1", "101", 2)
    service.add_room("D1", "102", 3)

    # Act
    rooms = service.get_all_rooms()

    # Assert
    assert len(rooms) == 2

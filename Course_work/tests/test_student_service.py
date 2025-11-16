import pytest
from BLL.student_service import StudentService
from BLL.student import Student
from BLL.exceptions import ValidationError, NotFoundError


class StubStudentCollection:
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
    return StudentService(StubStudentCollection())


def test_add_student_success(service):
    # Arrange
    name = "Ivan"
    surname = "Petrenko"
    sid = "AA001"
    gender = "M"

    # Act
    student = service.add_student(name, surname, sid, gender)

    # Assert
    assert student.name == name
    assert student.student_id == sid
    assert len(service.get_all()) == 1


def test_add_student_duplicate_id(service):
    # Arrange
    service.add_student("Ivan", "P", "AA003", "M")

    # Act / Assert
    with pytest.raises(ValidationError):
        service.add_student("Oleh", "I", "AA003", "M")


def test_delete_student_success(service):
    # Arrange
    service.add_student("Ivan", "P", "AA004", "M")

    # Act
    service.delete_student("AA004")

    # Assert
    assert len(service.get_all()) == 0


def test_delete_nonexistent_student(service):
    # Arrange — empty collection

    # Act / Assert
    with pytest.raises(NotFoundError):
        service.delete_student("XXX")


def test_update_student_success(service):
    # Arrange
    service.add_student("Ivan", "P", "AA005", "M")

    # Act
    updated = service.update_student("AA005", name="Oleh")

    # Assert
    assert updated.name == "Oleh"


def test_update_nonexistent_student(service):
    # Arrange — void

    # Act / Assert
    with pytest.raises(ValidationError):
        service.update_student("NOPE", name="Test")


def test_get_all_students(service):
    # Arrange
    service.add_student("A", "A", "AA006", "M")
    service.add_student("B", "B", "AA007", "F")

    # Act
    result = service.get_all()

    # Assert
    assert len(result) == 2


def test_get_by_id_success(service):
    # Arrange
    service.add_student("Ivan", "P", "AA008", "M")

    # Act
    st = service.get_by_id("AA008")

    # Assert
    assert st.surname == "P"


def test_get_by_id_not_found(service):
    # Arrange — none

    # Act / Assert
    with pytest.raises(ValidationError):
        service.get_by_id("NOPE")

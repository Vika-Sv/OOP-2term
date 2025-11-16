import pytest
from BLL.group_service import GroupService
from BLL.group import Group
from BLL.exceptions import ValidationError, NotFoundError
from BLL.generic_collection import Collection


# ===== FIXTURE =====

@pytest.fixture
def service():
    groups = Collection[Group]()
    return GroupService(groups)


# ===== TESTS =====

def test_add_group_success(service):
    # Arrange / Act
    group = service.add_group("Bachelor", "IPZ", 2024, "B-121", "SE")

    # Assert
    assert group.course == "B-121"
    assert group.major == "IPZ"
    assert group.year == 2024


def test_add_group_duplicate(service):
    # Arrange
    service.add_group("Bachelor", "IPZ", 2024, "B-122", "SE")

    # Act / Assert
    with pytest.raises(ValidationError):
        service.add_group("Bachelor", "IPZ", 2024, "B-122", "SE")


def test_remove_group_success(service):
    # Arrange
    service.add_group("Bachelor", "IPZ", 2024, "B-123", "SE")

    # Act
    service.delete_group("B-123")

    # Assert
    assert service.groups.get_all() == []


def test_remove_group_not_found(service):
    # Arrange / Act / Assert
    with pytest.raises(NotFoundError):
        service.delete_group("NOPE")


def test_update_group_success(service):
    # Arrange
    service.add_group("Bachelor", "IPZ", 2024, "B-124", "SE")

    # Act
    updated = service.update_group("B-124", major="CS")

    # Assert
    assert updated.major == "CS"


def test_update_group_not_found(service):
    # Arrange / Act / Assert
    with pytest.raises(NotFoundError):
        service.update_group("NOPE", major="CS")


def test_get_all_groups(service):
    # Arrange
    service.add_group("B", "IPZ", 1, "B-125", "SE")

    # Act
    res = service.get_all()

    # Assert
    assert len(res) == 1
    assert res[0].course == "B-125"


def test_get_group_by_id_success(service):
    # Arrange
    service.add_group("B", "IPZ", 1, "B-127", "SE")

    # Act
    g = service.get_by_id("B-127")

    # Assert
    assert g.course == "B-127"


def test_get_group_by_id_not_found(service):
    # Arrange / Act / Assert
    with pytest.raises(NotFoundError):
        service.get_by_id("NOPE")


def test_add_student_to_group(service):
    # Arrange
    service.add_group("B", "IPZ", 1, "B-128", "SE")
    group = service.get_by_id("B-128")

    # Act
    service.add_student_to_group(group, "AA001")

    # Assert
    assert "AA001" in group.students


def test_add_student_to_group_not_found(service):
    # Arrange / Act / Assert
    with pytest.raises(NotFoundError):
        service.add_student_to_group("NOPE", "AA001")


def test_remove_student_from_group(service):
    # Arrange
    service.add_group("B", "IPZ", 1, "B-129", "SE")
    group = service.get_by_id("B-129")
    group.students.append("AA002")

    # Act
    service.remove_student_from_group("B-129", "AA002")

    # Assert
    assert "AA002" not in group.students


def test_remove_student_from_group_not_found(service):
    # Arrange / Act / Assert
    with pytest.raises(NotFoundError):
        service.remove_student_from_group("NOPE", "AA001")



def test_update_group_nothing_changes(service):
    # Arrange
    g = service.add_group("B", "IPZ", 2024, "B-130", "SE")

    # Act
    updated = service.update_group("B-130")

    # Assert
    assert updated.degree == "B"
    assert updated.major == "IPZ"
    assert updated.year == 2024
    assert updated.educational_program == "SE"


def test_get_all_groups_empty(service):
    # Arrange — порожня колекція

    # Act
    res = service.get_all()

    # Assert
    assert res == []


def test_group_str_representation(service):
    # Arrange
    g = service.add_group("B", "IPZ", 2024, "B-131", "SE")

    # Act
    text = str(g)

    # Assert
    assert "B-131" in text
    assert "IPZ" in text

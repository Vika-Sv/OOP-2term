from BLL.generic_collection import Collection
from BLL.student_service import StudentService
from BLL.group_service import GroupService
from BLL.dorm_service import DormService

from DAL.student_data import StudentData
from DAL.group_data import GroupData
from DAL.dorm_data import DormData

from PL.menu import Menu


def main():
    student_data = StudentData()
    group_data = GroupData()
    dorm_data = DormData()

    students_list = student_data.load_all()
    groups_list = group_data.load_all()
    dorm_list = dorm_data.load_all()

   
    students = Collection()
    students._items = students_list

    groups = Collection()
    groups._items = groups_list

    dorm = Collection()
    dorm._items = dorm_list

   
    student_service = StudentService(students)
    group_service = GroupService(groups)
    dorm_service = DormService(dorm)


    menu = Menu(student_service, group_service, dorm_service)
    menu.run()

    
    student_data.save_all(students.get_all())
    group_data.save_all(groups.get_all())
    dorm_data.save_all(dorm.get_all())


if __name__ == "__main__":
    main()

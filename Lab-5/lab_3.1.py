from DAL.database import Database
from PL.ConsoleMenu import ConsoleMenu
from BLL.student_logic import StudentLogic

if __name__ == "__main__":
    repository = Database()
    logic = StudentLogic(repository)
    menu = ConsoleMenu(logic)
    menu.menu()

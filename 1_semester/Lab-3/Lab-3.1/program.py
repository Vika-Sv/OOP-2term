from DAL.entity_context import EntityContext
from BLL.entity_service import EntityService
from PL.menu import Menu

class Program:
    @staticmethod
    def Main():
        context = EntityContext()
        service = EntityService(context)
        menu = Menu(service)
        menu.main_menu()

if __name__ == "__main__":
    Program.Main()

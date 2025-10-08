from database import Database
from ConsoleMenu import ConsoleMenu


if __name__ == "__main__":
    db = Database()
    menu = ConsoleMenu(db)
    menu.menu()


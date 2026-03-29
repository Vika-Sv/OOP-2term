class Student:
    def __init__(self, last_name: str, first_name: str, course: int, student_id: int, served_in_army: bool):
        self.last_name = last_name          # Прізвище
        self.first_name = first_name        # Ім'я
        self.course = course                # Курс
        self.student_id = student_id        # Студентський квиток (ключ BST)
        self.served_in_army = served_in_army  # Служба в армії
 
    def __str__(self):
        army = "Так" if self.served_in_army else "Ні"
        return (f"  {self.student_id:<10} {self.last_name:<15} {self.first_name:<12}"
                f" {self.course:<7} {army}")
class Student:
    def __init__(self, last_name: str, first_name: str, course: int, student_id: int, served_in_army: bool):
        self.last_name = last_name         
        self.first_name = first_name      
        self.course = course               
        self.student_id = student_id       
        self.served_in_army = served_in_army 
 
    def __str__(self):
        army = "Так" if self.served_in_army else "Ні"
        return (f"  {self.student_id:<10} {self.last_name:<15} {self.first_name:<12}"
                f" {self.course:<7} {army}")
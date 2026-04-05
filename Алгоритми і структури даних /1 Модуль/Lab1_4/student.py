class Student:
    def __init__(self, surname, name, group, faculty):
        self.surname = surname
        self.name = name
        self.group = group
        self.faculty = faculty  

    def __str__(self):
        return f"Group: {self.group}, Faculty: {self.faculty}, Student: {self.surname} {self.name}"
    

    
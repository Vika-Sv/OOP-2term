class Student: 
    def __init__(self, name, dateOfBirth, hobby): 
        self.name = name 
        self.dateOfBirth = dateOfBirth 
        self.hobby = hobby 

    def get_info(self): 
        return f"Name: {self.name}, Date of Birth: {self.dateOfBirth}, Hobby: {self.hobby}"
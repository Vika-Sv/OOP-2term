class Database:
    def __init__(self, filename='database.txt'):
        self.filename = filename

    def save(self, persons):
        with open(self.filename, 'w', encoding='utf-8') as f:
            for s in persons:
                ObjectName = s.FirstName + s.LastName
                f.write(f"Student {ObjectName}\n")
                f.write("{\n")
                f.write(f'"Firstname": "{s.FirstName}",\n')
                f.write(f'"Lastname": "{s.LastName}",\n')
                f.write(f'"StudentId": "{s.StudentID}",\n')
                f.write(f'"Course": "{s.Course}",\n')
                f.write(f'"Gender": "{s.Gender}",\n')
                f.write(f'"Adress": "{s.Adress}"\n')
                f.write("};\n")

    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return f.readlines()
        except FileNotFoundError:
            return []

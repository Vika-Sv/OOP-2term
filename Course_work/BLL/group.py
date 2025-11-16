class Group:
    def __init__(self, degree, major, year, course, educational_program):
        self._degree = degree
        self._major = major
        self._year = year
        self._course = course
        self._educational_program = educational_program
        self._students = []  

    @property
    def course(self):
        return self._course

    @property
    def degree(self):
        return self._degree

    @property
    def major(self):
        return self._major

    @property
    def year(self):
        return self._year

    @property
    def educational_program(self):
        return self._educational_program

    @property
    def students(self):
        return self._students

  
    def add_student(self, student_id):
        if student_id not in self._students:
            self._students.append(student_id)

    
    def remove_student(self, student_id):
        if student_id in self._students:
            self._students.remove(student_id)
            
            
    def to_dict(self) -> dict:
        return {
            "degree": self.degree,
            "major": self.major,
            "year": self.year,
            "course": self.course,
            "educational_program": self.educational_program,
            "students": list(self.students),
        }

    @staticmethod
    def from_dict(d: dict) -> "Group":
        g = Group(
            degree=d["degree"],
            major=d["major"],
            year=d["year"],
            course=d["course"],
            educational_program=d["educational_program"],
        )
        for sid in d.get("students", []):
            g.add_student(sid)
        return g        

    def __str__(self):
        return f"{self._degree}-{self._major}-{self._year}-{self._course}-{self._educational_program}"

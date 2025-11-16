class Group:
    def __init__(self, degree, major, year, course, educational_program):
        self._degree = degree
        self._major = major
        self._year = year
        self._course = course
        self._educational_program = educational_program
        self._students = []  # список student_id

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

    # =============================
    # 👉 ДОДАТИ СТУДЕНТА ДО ГРУПИ
    # =============================
    def add_student(self, student_id):
        if student_id not in self._students:
            self._students.append(student_id)

    # =============================
    # 👉 ВИДАЛИТИ СТУДЕНТА З ГРУПИ
    # =============================
    def remove_student(self, student_id):
        if student_id in self._students:
            self._students.remove(student_id)

    def __str__(self):
        return f"{self._degree}-{self._major}-{self._year}-{self._course}-{self._educational_program}"

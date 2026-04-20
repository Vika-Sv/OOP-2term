class Student: 
    def __init__(self, first_name, last_name, day, month, year, hobby): 
        self.first_name = first_name
        self.last_name = last_name
        self.day = day
        self.month = month
        self.year = year
        self.hobby = hobby

    def birth_key(self) -> int:
        return self.year * 10000 + self.month * 100 + self.day
 
    def birth_str(self) -> str:
        return f"{self.day:02d}.{self.month:02d}.{self.year}"
 
    def is_born_in_summer(self) -> bool:
        return self.month in (6, 7, 8)
 
    def likes_tourism(self) -> bool:
        return self.hobby.lower() == "туризм"
    

    def __str__(self):
        return (f"{self.last_name} {self.first_name} | " f"Народжений: {self.day:02d}.{self.month:02d}.{self.year} | " f"Хобі: {self.hobby}")

class MyString:
    def __init__(self, value: str):
        self.value = value
        self.length = len(value)

    def find_substring(self, sub: str) -> int:
        return self.value.find(sub)

    def insert_substring(self, sub: str, pos: int):
        if 0 <= pos <= len(self.value):
            self.value = self.value[:pos] + sub + self.value[pos:]
            self.length = len(self.value)

    def replace_substring(self, old: str, new: str):
        self.value = self.value.replace(old, new)
        self.length = len(self.value)

    def display(self):
        return self.value

    def __str__(self):
        return self.value

    def to_dict(self):
        return {"value": self.value, "length": self.length}

    @staticmethod
    def from_dict(data: dict):
        return MyString(data["value"])

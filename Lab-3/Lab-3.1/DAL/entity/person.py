from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
    
    @abstractmethod
    def info(self):
        pass

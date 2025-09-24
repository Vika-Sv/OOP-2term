from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, FirstName,LastName):
        self.FirstName = FirstName
        self.LastName = LastName
    
    
    @abstractmethod
    def info(self):
            pass
    
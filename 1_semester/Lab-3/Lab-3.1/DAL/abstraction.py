from abc import ABC, abstractmethod

class Abstraction(ABC):
    @abstractmethod
    def save(self, data, filename):
        pass

    @abstractmethod
    def load(self, filename):
        pass

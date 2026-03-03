from Animal import Animal
from Habitet import Habitat

class Dog(Animal):
    def __init__(self, name: str, habitat: Habitat = Habitat.OWNER):
        super().__init__(name, eyes=2, legs=4, wings=0, habitat=habitat)

    def kind(self) -> str:
        return "Dog"
from Animal import Animal
from Habitet import Habitat

class Owl(Animal):
    def __init__(self, name: str, habitat: Habitat = Habitat.OWNER):
        super().__init__(name, eyes=2, legs=2, wings=2, habitat=habitat)

    def kind(self) -> str:
        return "Owl"
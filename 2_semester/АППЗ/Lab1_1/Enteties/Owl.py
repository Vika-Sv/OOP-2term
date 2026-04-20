from Enteties.Animal import Animal, Habitat

class Owl(Animal):
    def __init__(self, name: str, habitat: Habitat = Habitat.OWNER):
        super().__init__(name, eyes=2, legs=2, wings=2, habitat=habitat)

    def kind(self) -> str:
        return "Owl"
    
    def move_verb(self) -> str:
        return "walks"
from Enteties.Animal import Animal, Habitat

class Lizard(Animal):
    def __init__(self, name: str, habitat: Habitat = Habitat.WILD):
        super().__init__(name, eyes=2, legs=4, wings=0, habitat=habitat)

    def kind(self) -> str:
        return "Lizard"
    
    def move_verb(self) -> str:
        return "crawls"
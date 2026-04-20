from Entities.Animal import Animal, Habitat

class Dog(Animal):
    def __init__(self, name: str, habitat: Habitat = Habitat.OWNER):
        super().__init__(name, eyes=2, legs=4, wings=0, habitat=habitat)

    def kind(self) -> str:
        return "Dog"

    def move_verb(self) -> str:
        return "walks"

class Owl(Animal):
    def __init__(self, name: str, habitat: Habitat = Habitat.OWNER):
        super().__init__(name, eyes=2, legs=2, wings=2, habitat=habitat)

    def kind(self) -> str:
        return "Owl"

    def move_verb(self) -> str:
        return "walks"

class Lizard(Animal):
    def __init__(self, name: str, habitat: Habitat = Habitat.WILD):
        super().__init__(name, eyes=2, legs=4, wings=0, habitat=habitat)

    def kind(self) -> str:
        return "Lizard"

    def move_verb(self) -> str:
        return "crawls"

from abc import ABC, abstractmethod
from Entities.Animal import Animal, Habitat
from Entities.Animals import Dog, Owl, Lizard

class IAnimalFactory(ABC):
    @abstractmethod
    def create_dog(self, name: str) -> Animal: ...

    @abstractmethod
    def create_owl(self, name: str) -> Animal: ...

    @abstractmethod
    def create_lizard(self, name: str) -> Animal: ...

    @abstractmethod
    def create_custom(self, name: str, species: str,eyes: int, legs: int, wings: int) -> Animal: ...


class OwnerAnimalFactory(IAnimalFactory):
    def create_dog(self, name: str) -> Animal:
        return Dog(name, Habitat.OWNER)

    def create_owl(self, name: str) -> Animal:
        return Owl(name, Habitat.OWNER)

    def create_lizard(self, name: str) -> Animal:
        return Lizard(name, Habitat.OWNER)

    def create_custom(self, name: str, species: str, eyes: int, legs: int, wings: int) -> Animal:
        return _make_custom(name, species, eyes, legs, wings, Habitat.OWNER)


class PetShopAnimalFactory(IAnimalFactory):
    def create_dog(self, name: str) -> Animal:
        return Dog(name, Habitat.PET_SHOP)

    def create_owl(self, name: str) -> Animal:
        return Owl(name, Habitat.PET_SHOP)

    def create_lizard(self, name: str) -> Animal:
        return Lizard(name, Habitat.PET_SHOP)

    def create_custom(self, name: str, species: str, eyes: int, legs: int, wings: int) -> Animal:
        return _make_custom(name, species, eyes, legs, wings, Habitat.PET_SHOP)


class WildAnimalFactory(IAnimalFactory):
    def create_dog(self, name: str) -> Animal:
        return Dog(name, Habitat.WILD)

    def create_owl(self, name: str) -> Animal:
        return Owl(name, Habitat.WILD)

    def create_lizard(self, name: str) -> Animal:
        return Lizard(name, Habitat.WILD)

    def create_custom(self, name: str, species: str, eyes: int, legs: int, wings: int) -> Animal:
        return _make_custom(name, species, eyes, legs, wings, Habitat.WILD)

def _make_custom(name: str, species: str, eyes: int, legs: int, wings: int, habitat: Habitat) -> Animal:
    cls = type(species, (Animal,), {
        "kind":      lambda self: species,
        "move_verb": lambda self: "moves",
    })
    return cls(name, eyes=eyes, legs=legs, wings=wings, habitat=habitat)

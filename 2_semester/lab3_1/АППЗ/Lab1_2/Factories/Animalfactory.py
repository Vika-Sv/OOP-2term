from abc import ABC, abstractmethod

from Enteties.Animal import Animal, Habitat
from Enteties.Dog import Dog
from Enteties.Owl import Owl
from Enteties.Lizard import Lizard


class AnimalFactory(ABC):
    @abstractmethod
    def create(self, name: str, habitat: Habitat) -> Animal:
        pass


class DogFactory(AnimalFactory):
    def create(self, name: str, habitat: Habitat = Habitat.OWNER) -> Animal:
        return Dog(name, habitat)


class OwlFactory(AnimalFactory):
    def create(self, name: str, habitat: Habitat = Habitat.OWNER) -> Animal:
        return Owl(name, habitat)


class LizardFactory(AnimalFactory):
    def create(self, name: str, habitat: Habitat = Habitat.WILD) -> Animal:
        return Lizard(name, habitat)


class CustomFactory(AnimalFactory):
    def __init__(self, species: str, eyes: int, legs: int, wings: int):
        self._species = species
        self._eyes    = eyes
        self._legs    = legs
        self._wings   = wings

    def create(self, name: str, habitat: Habitat = Habitat.OWNER) -> Animal:
        species  = self._species
        eyes     = self._eyes
        legs     = self._legs
        wings    = self._wings

        CustomAnimal = type(species, (Animal,), {
            "kind":      lambda self: species,
            "move_verb": lambda self: "moves",
        })
        return CustomAnimal(name, eyes=eyes, legs=legs, wings=wings, habitat=habitat)


FACTORIES: dict[str, AnimalFactory] = {
    "Dog":    DogFactory(),
    "Owl":    OwlFactory(),
    "Lizard": LizardFactory(),
}
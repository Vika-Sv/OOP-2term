from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class Habitat(Enum):
    OWNER = "owner's home"
    PET_SHOP = "pet shop"
    WILD = "wild"


class Animal(ABC):
    MAX_MEALS = 5
    MIN_MEALS = 1
    HUNGER_HOURS = 8

    def __init__(self, name: str, eyes: int, legs: int, wings: int, habitat: Habitat):
        self.name = name
        self.eyes = eyes
        self.legs = legs
        self.wings = wings
        self.habitat = habitat

        self._alive: bool = True
        self._happy: bool = (habitat == Habitat.WILD)
        self._meals: list[datetime] = []
        self._last_meal: datetime | None = None
        self._cleanings: int = 0
        self._day_start: datetime = datetime.now()

    @property
    def alive(self) -> bool:
        return self._alive

    @property
    def happy(self) -> bool:
        return self._happy

    @property
    def hungry(self) -> bool:
        if not self._last_meal:
            return True
        hrs = (datetime.now() - self._last_meal).total_seconds() / 3600
        return hrs >= self.HUNGER_HOURS

    @property
    def meals_today(self) -> int:
        return len(self._meals)

    @abstractmethod
    def kind(self) -> str:
        pass

    @abstractmethod
    def move_verb(self) -> str:
        pass

from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from Events.event import Event
from Events.eventArgs import HungryEventArgs, DiedEventArgs, HappyChangedEventArgs

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

        self._alive = True
        self._happy = (habitat == Habitat.WILD)
        self._meals:list[datetime] = []
        self._last_meal: datetime | None = None
        self._cleanings = 0
        self._day_start = datetime.now()

        self.hungry_event:       Event[HungryEventArgs]       = Event()
        self.died_event:         Event[DiedEventArgs]         = Event()
        self.happy_changed_event: Event[HappyChangedEventArgs] = Event()

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
 
    def _mark_eaten(self) -> None:
        now = datetime.now()
        self._meals.append(now)
        self._last_meal = now
 
    def _mark_dead(self, reason: str) -> None:
        self._alive = False
        self.died_event.fire(self, DiedEventArgs(self, reason))
 
    def _set_happy(self, value: bool) -> None:
        if value != self._happy:
            self._happy = value
            self.happy_changed_event.fire(self, HappyChangedEventArgs(self, value))
 
    def _reset_day(self) -> None:
        self._meals.clear()
        self._cleanings = 0
        self._day_start = datetime.now()
 
    def _add_cleaning(self) -> None:
        self._cleanings += 1
 
    @abstractmethod
    def kind(self) -> str:
        pass
 
    @abstractmethod
    def move_verb(self) -> str:
        pass
 
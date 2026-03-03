from abc import ABC, abstractmethod
from datetime import datetime
from Habitet import Habitat


class Animal(ABC):

    MAX_MEALS    = 5
    MIN_MEALS    = 1
    HUNGER_HOURS = 8

    def __init__(self, name: str, eyes: int, legs: int, wings: int, habitat: Habitat):
        self.name    = name
        self.eyes    = eyes
        self.legs    = legs
        self.wings   = wings
        self.habitat = habitat

        self._alive     = True
        self._happy     = (habitat == Habitat.WILD)
        self._meals:    list[datetime] = []
        self._last_meal: datetime | None = None
        self._cleanings = 0
        self._day_start = datetime.now()

        # events
        self._on_hungry:       list = []
        self._on_died:         list = []
        self._on_happy_change: list = []

    # -- event subscription --

    def on_hungry(self, cb):       self._on_hungry.append(cb)
    def off_hungry(self, cb):      self._on_hungry.remove(cb)
    def on_died(self, cb):         self._on_died.append(cb)
    def on_happy_change(self, cb): self._on_happy_change.append(cb)

    # -- properties --

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

    # -- internal logic --

    def _tick_day(self):
        """Check if a day has passed and reset counters."""
        if (datetime.now() - self._day_start).total_seconds() >= 30:  # 30s = 1 day for demo
            if len(self._meals) < self.MIN_MEALS and self._alive:
                self._alive = False
                for cb in self._on_died:
                    cb(self, "starved (0 meals in a day)")
            self._meals.clear()
            self._cleanings = 0
            self._day_start = datetime.now()

    def _set_happy(self, value: bool):
        if value != self._happy:
            self._happy = value
            for cb in self._on_happy_change:
                cb(self, value)

    # -- actions --

    def eat(self) -> bool:
        self._tick_day()
        if not self._alive or len(self._meals) >= self.MAX_MEALS:
            return False
        self._meals.append(datetime.now())
        self._last_meal = datetime.now()
        return True

    def clean(self) -> bool:
        if not self._alive or self.habitat == Habitat.WILD:
            return False
        self._tick_day()
        self._cleanings += 1
        self._set_happy(True)
        return True

    def run(self) -> bool:
        return self._alive and not self.hungry

    def fly(self) -> bool:
        return self._alive and self.wings > 0 and not self.hungry

    def walk(self) -> bool:
        return self._alive

    @abstractmethod
    def kind(self) -> str:
        """Species name."""
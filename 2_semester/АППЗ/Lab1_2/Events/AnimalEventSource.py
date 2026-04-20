from Events.Event import Event
from Events.EventArgs import (
    HungryEventArgs,
    DiedEventArgs,
    HappyChangedEventArgs,
    FedEventArgs,
)
from Entities.Animal import Animal


class AnimalEventSource:
    def __init__(self, animal: Animal):
        self._animal = animal

        self.on_hungry       : Event[HungryEventArgs]       = Event()
        self.on_died         : Event[DiedEventArgs]         = Event()
        self.on_happy_changed: Event[HappyChangedEventArgs] = Event()
        self.on_fed          : Event[FedEventArgs]          = Event()

    @property
    def animal(self) -> Animal:
        return self._animal

    def fire_hungry(self) -> None:
        self.on_hungry.fire(HungryEventArgs(self._animal))

    def fire_died(self, reason: str) -> None:
        self.on_died.fire(DiedEventArgs(self._animal, reason))

    def fire_happy_changed(self, is_happy: bool) -> None:
        self.on_happy_changed.fire(HappyChangedEventArgs(self._animal, is_happy))

    def fire_fed(self) -> None:
        self.on_fed.fire(FedEventArgs(self._animal, self._animal.meals_today))

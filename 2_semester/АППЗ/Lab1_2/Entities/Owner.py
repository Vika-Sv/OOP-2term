from Entities.Animal import Animal
from Events.AnimalEventSource import AnimalEventSource
from Events.EventArgs import (HungryEventArgs, DiedEventArgs, HappyChangedEventArgs,FedEventArgs)

class Owner:
    def __init__(self, name: str):
        self.name = name
        self._entries: list[tuple[Animal, AnimalEventSource]] = []

    def adopt(self, animal: Animal, source: AnimalEventSource) -> None:
        source.on_hungry += self._handle_hungry
        source.on_died += self._handle_died
        source.on_happy_changed += self._handle_happy_changed
        source.on_fed += self._handle_fed
        self._entries.append((animal, source))

    def release(self, animal: Animal) -> None:
        entry = self._find_entry(animal)
        if entry is None:
            return
        _, source = entry
        source.on_hungry -= self._handle_hungry
        source.on_died -= self._handle_died
        source.on_happy_changed -= self._handle_happy_changed
        source.on_fed -= self._handle_fed
        self._entries.remove(entry)

    @property
    def animals(self) -> list[Animal]:
        return [a for a, _ in self._entries]

    @property
    def entries(self) -> list[tuple[Animal, AnimalEventSource]]:
        return list(self._entries)

    def get_source(self, animal: Animal) -> AnimalEventSource | None:
        entry = self._find_entry(animal)
        return entry[1] if entry else None


    def _handle_hungry(self, args: HungryEventArgs) -> None:
        self._notify(f"{args.animal.name} is hungry!")

    def _handle_died(self, args: DiedEventArgs) -> None:
        self._notify(f"{args.animal.name} has died! Reason: {args.reason}")

    def _handle_happy_changed(self, args: HappyChangedEventArgs) -> None:
        state = "happy" if args.is_happy else "unhappy"
        self._notify(f"{args.animal.name} is now {state}.")

    def _handle_fed(self, args: FedEventArgs) -> None:
        self._notify(f"{args.animal.name} ate. Meals today: {args.meals_today}/{args.animal.MAX_MEALS}")


    def _notify(self, message: str) -> None:
        self.pending_notifications.append(f"[{self.name}] {message}")

    def _find_entry(self, animal: Animal):
        for entry in self._entries:
            if entry[0] is animal:
                return entry
        return None
    pending_notifications: list 

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def __init__(self, name: str):
        self.name = name
        self._entries: list[tuple[Animal, AnimalEventSource]] = []
        self.pending_notifications: list[str] = []

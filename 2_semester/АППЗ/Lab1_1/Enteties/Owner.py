from Enteties.Animal import Animal

class Owner:
    def __init__(self, name: str):
        self.name = name
        self._animals: list[Animal] = []

    def adopt(self, animal: Animal):
        animal.on_hungry(self._notify_hungry)
        animal.on_died(self._notify_died)
        animal.on_happy_change(self._notify_happy)
        self._animals.append(animal)

    def release(self, animal: Animal):
        animal.off_hungry(self._notify_hungry)
        self._animals.remove(animal)

    @property
    def animals(self):
        return list(self._animals)

    def _notify_hungry(self, a: Animal):
        print(f"\n  [NOTIFICATION] {self.name}: {a.name} is hungry!")

    def _notify_died(self, a: Animal, reason: str):
        print(f"\n  [NOTIFICATION] {self.name}: {a.name} has died! Reason: {reason}")

    def _notify_happy(self, a: Animal, is_happy: bool):
        state = "happy" if is_happy else "unhappy"
        print(f"\n  [NOTIFICATION] {self.name}: {a.name} is now {state}.")
from datetime import datetime

from Enteties.Animal import Animal, Habitat
from Events.eventArgs import HungryEventArgs


DAY_SECONDS = 600


class AnimalService:

    @staticmethod
    def tick(animal: Animal) -> None:
        if not animal.alive:
            return

        elapsed = (datetime.now() - animal._day_start).total_seconds()
        if elapsed >= DAY_SECONDS:
            if animal.meals_today < animal.MIN_MEALS:
                animal._mark_dead("starved (0 meals in a day)")
            else:
                animal._reset_day()

        if animal.alive and animal.hungry:
            animal.hungry_event.fire(animal, HungryEventArgs(animal))

    @staticmethod
    def eat(animal: Animal) -> bool:
        if not animal.alive or animal.meals_today >= animal.MAX_MEALS:
            return False
        animal._mark_eaten()
        return True

    @staticmethod
    def clean(animal: Animal) -> bool:
        if not animal.alive or animal.habitat == Habitat.WILD:
            return False
        animal._add_cleaning()
        animal._set_happy(True)
        return True

    @staticmethod
    def run(animal: Animal) -> bool:
        return animal.alive and not animal.hungry

    @staticmethod
    def fly(animal: Animal) -> bool:
        return animal.alive and animal.wings > 0 and not animal.hungry
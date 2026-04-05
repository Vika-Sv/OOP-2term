from datetime import datetime
from Enteties.Animal import Animal, Habitat

class AnimalService:
    def _tick_day(animal: Animal):
        if (datetime.now() - animal._day_start).total_seconds() >= 600: # if pet didn't eat for 10 minutes, it dies of hunger (for testing purposes, 1 = 1 hour) 
            if len(animal._meals) < animal.MIN_MEALS and animal._alive:
                animal._alive = False
                for cb in animal._on_died:
                    cb(animal, "starved (0 meals in a day)")
            animal._meals.clear()
            animal._cleanings = 0
            animal._day_start = datetime.now()

    def _set_happy(animal: Animal, value: bool):
        if value != animal._happy:
            animal._happy = value
            for cb in animal._on_happy_change:
                cb(animal, value)


    @staticmethod
    def eat(animal: Animal) -> bool:
        AnimalService._tick_day(animal)
        if not animal._alive or len(animal._meals) >= animal.MAX_MEALS:
            return False
        animal._meals.append(datetime.now())
        animal._last_meal = datetime.now()
        return True

    @staticmethod
    def clean(animal: Animal) -> bool:
        if not animal._alive or animal.habitat == Habitat.WILD:
            return False
        AnimalService._tick_day(animal)
        animal._cleanings += 1
        AnimalService._set_happy(animal, True)
        return True

    @staticmethod
    def run(animal: Animal) -> str | None:
        return animal._alive and not animal.hungry

    @staticmethod
    def fly(animal: Animal) -> bool:
        return animal._alive and animal.wings > 0 and not animal.hungry
from datetime import datetime
from Entities.Animal import Animal, Habitat
from Events.AnimalEventSource import AnimalEventSource


class AnimalService:
    @staticmethod
    def tick_day(animal: Animal, source: AnimalEventSource) -> None:
        elapsed = (datetime.now() - animal._day_start).total_seconds()
        if elapsed < 600:       
            return

        if animal._alive and animal.meals_today < animal.MIN_MEALS:
            animal._alive = False
            source.fire_died("starved — 0 meals in a day")
            
        if animal.meals_today >= animal.MIN_MEALS:
            intervals = [
                (animal._meals[i+1] - animal._meals[i]).total_seconds()
                for i in range(len(animal._meals) - 1)
            ]
        if intervals:
            avg = sum(intervals) / len(intervals)
        for interval in intervals:
            if abs(interval - avg) > avg * 0.5:
                animal._alive = False
                source.fire_died("irregular feeding schedule")

        animal._meals.clear()
        animal._cleanings = 0
        animal._day_start = datetime.now()

    @staticmethod
    def check_hunger(animal: Animal, source: AnimalEventSource) -> None:
        if animal._alive and animal.hungry:
            source.fire_hungry()

    @staticmethod
    def eat(animal: Animal, source: AnimalEventSource) -> bool:
        if not animal._alive:
            return False
        if animal.meals_today >= animal.MAX_MEALS:
            return False

        animal._meals.append(datetime.now())
        animal._last_meal = datetime.now()
        source.fire_fed()
        return True

    @staticmethod
    def clean(animal: Animal, source: AnimalEventSource) -> bool:
        if not animal._alive or animal.habitat == Habitat.WILD:
            return False

        animal._cleanings += 1
        AnimalService._update_happy(animal, source)
        return True

    @staticmethod
    def run(animal: Animal) -> bool:
        return animal._alive and not animal.hungry

    @staticmethod
    def fly(animal: Animal) -> bool:
        return animal._alive and animal.wings > 0 and not animal.hungry


    @staticmethod
    def _update_happy(animal: Animal, source: AnimalEventSource) -> None:
        should_be_happy = (
            animal.habitat == Habitat.WILD
            or animal._cleanings >= 1
        )
        if should_be_happy != animal._happy:
            animal._happy = should_be_happy
            source.fire_happy_changed(should_be_happy)

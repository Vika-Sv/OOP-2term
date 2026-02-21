class Wild:
    @staticmethod
    def release(animal: Animal, current_pets: List[Animal]):
        if animal in current_pets:
            current_pets.remove(animal)
        animal.is_happy = True # Requirement: Always happy in the wild
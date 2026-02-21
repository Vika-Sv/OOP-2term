class PetShop:
    def __init__(self, name: str):
        self.name = name
        self.stock: List[Animal] = []
        self.care = CareService()

    def receive_animal(self, animal: Animal):
        self.stock.append(animal)
        self.care.update_happiness(self.stock)
class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Animal] = []
        self.home_care = CareService()

    def adopt(self, animal: Animal, from_shop: Optional[PetShop] = None):
        if from_shop and animal in from_shop.stock:
            from_shop.stock.remove(animal)
        self.pets.append(animal)
        self.home_care.update_happiness(self.pets)
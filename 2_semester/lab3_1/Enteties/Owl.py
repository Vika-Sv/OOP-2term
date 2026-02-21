class Owl(Animal):
    def __init__(self, name: str):
        super().__init__(name, FlyStrategy(), eyes=2, paws=2, wings=2)
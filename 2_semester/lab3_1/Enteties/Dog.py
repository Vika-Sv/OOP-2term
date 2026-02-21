class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name, RunStrategy(), eyes=2, paws=4, wings=0)
class EventArgs:
    pass


class HungryEventArgs(EventArgs):
    def __init__(self, animal):
        self.animal = animal


class DiedEventArgs(EventArgs):
    def __init__(self, animal, reason: str):
        self.animal = animal
        self.reason = reason


class HappyChangedEventArgs(EventArgs):
    def __init__(self, animal, is_happy: bool):
        self.animal = animal
        self.is_happy = is_happy
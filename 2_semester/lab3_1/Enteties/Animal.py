class Animal(ABC):
    def __init__(self, name: str, movement: MovementStrategy, 
                 eyes: int, paws: int, wings: int):
        self.name = name
        self.eyes = eyes
        self.paws = paws
        self.wings = wings
        
        # State properties
        self._movement_strategy = movement
        self._is_alive = True
        self._is_happy = False
        self.last_meal_time = datetime.datetime.now()
        self.meals_today = 0
        
        # Events (No print statements inside)
        self.on_state_changed = Event()
        self.on_death = Event()

    @property
    def is_alive(self): return self._is_alive

    @property
    def is_happy(self): return self._is_happy

    @is_happy.setter
    def is_happy(self, value: bool):
        if self._is_happy != value:
            self._is_happy = value
            self.on_state_changed.trigger(f"{self.name} is now {'happy' if value else 'sad'}.")

    def eat(self):
        if not self._is_alive: return
        
        # Rule: Max 5 meals per day
        if self.meals_today < 5:
            self.meals_today += 1
            self.last_meal_time = datetime.datetime.now()
            self.on_state_changed.trigger(f"{self.name} consumed food. Total today: {self.meals_today}")
        else:
            self.on_state_changed.trigger(f"{self.name} is overfed and refuses to eat.")

    def perform_activity(self):
        if not self._is_alive: return
        
        # Rule: Hunger > 8 hours limits movement
        hours_since_meal = (datetime.datetime.now() - self.last_meal_time).total_seconds() / 3600
        
        if hours_since_meal > 8:
            action = f"{self.name} is too hungry to use normal skills, only {CrawlStrategy().move()}"
        else:
            action = f"{self.name} {self._movement_strategy.move()}"
        
        self.on_state_changed.trigger(action)

    def check_survival(self):
        """Validates survival conditions (1-5 meals per day)."""
        if not self._is_alive: return
        
        if self.meals_today < 1 or self.meals_today > 5:
            self._is_alive = False
            self.on_death.trigger(self.name, "incorrect feeding cycle")
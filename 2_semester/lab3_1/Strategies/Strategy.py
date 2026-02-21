class MovementStrategy(ABC):
    @abstractmethod
    def move(self) -> str: pass

class FlyStrategy(MovementStrategy):
    def move(self): return "flying in the heights"

class RunStrategy(MovementStrategy):
    def move(self): return "running fast"

class CrawlStrategy(MovementStrategy):
    def move(self): return "crawling on the ground"
class Event:
    """Implementation of the Observer pattern for decoupled communication."""
    def __init__(self):
        self._handlers: List[Callable] = []

    def subscribe(self, handler: Callable):
        if handler not in self._handlers:
            self._handlers.append(handler)

    def unsubscribe(self, handler: Callable):
        if handler in self._handlers:
            self._handlers.remove(handler)

    def trigger(self, *args, **kwargs):
        for handler in self._handlers:
            handler(*args, **kwargs)
from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class Event(Generic[T]):
    def __init__(self):
        self._handlers: list[Callable[[object, T], None]] = []

    def subscribe(self, handler: Callable[[object, T], None]) -> None:
        if handler not in self._handlers:
            self._handlers.append(handler)

    def unsubscribe(self, handler: Callable[[object, T], None]) -> None:
        if handler in self._handlers:
            self._handlers.remove(handler)

    def fire(self, sender: object, args: T) -> None:
        for handler in list(self._handlers):
            handler(sender, args)

    def __iadd__(self, handler):
        self.subscribe(handler)
        return self

    def __isub__(self, handler):
        self.unsubscribe(handler)
        return self
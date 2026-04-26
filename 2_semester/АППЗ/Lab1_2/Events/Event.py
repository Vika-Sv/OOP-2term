from typing import Callable, Generic, TypeVar

T = TypeVar("T")

class Event(Generic[T]):
    def __init__(self):
        self._handlers: list[Callable[[T], None]] = []

    def __iadd__(self, handler: Callable[[T], None]) -> "Event[T]": # Add handler: =+ operator in Owner.py
        if handler not in self._handlers:
            self._handlers.append(handler)
        return self

    def __isub__(self, handler: Callable[[T], None]) -> "Event[T]": # Remove handler: =- operator in Owner.py
        if handler in self._handlers:
            self._handlers.remove(handler)
        return self

    def fire(self, args: T) -> None:
        for handler in list(self._handlers):
            handler(args)

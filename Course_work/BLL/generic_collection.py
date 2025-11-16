from typing import Generic, TypeVar, List

T = TypeVar("T")

class Collection(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def add(self, obj: T):
        self._items.append(obj)

    def get_all(self) -> List[T]:
        return list(self._items)

    def find(self, predicate):
        for obj in self._items:
            if predicate(obj):
                return obj
        return None

    def find_all(self, predicate):
        return [obj for obj in self._items if predicate(obj)]

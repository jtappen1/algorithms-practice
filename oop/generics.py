
from typing import TypeVar, Generic, List

T = TypeVar("T")

class Repository(Generic[T]):

    def __init__(self):
        self.items : List[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get(self, index: int) -> T:
        return self.items[index]

    def remove(self, item: T) -> None:
        self.items.remove(item)

    def all(self) -> List[T]:
        return self.items
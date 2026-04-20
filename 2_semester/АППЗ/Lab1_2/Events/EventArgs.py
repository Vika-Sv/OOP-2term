from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Entities.Animal import Animal


@dataclass
class HungryEventArgs:
    animal: "Animal"

@dataclass
class DiedEventArgs:
    animal: "Animal"
    reason: str

@dataclass
class HappyChangedEventArgs:
    animal: "Animal"
    is_happy: bool

@dataclass
class FedEventArgs:
    animal: "Animal"
    meals_today: int

from typing import Protocol,runtime_checkable
from .Card import Card

@runtime_checkable
class CardList(Protocol):
    def pop_card(self)->Card:
        ...
    def cards_left(self)->int:
        ...


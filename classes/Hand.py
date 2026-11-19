from .Card_list_Protocol import CardList,Card,runtime_checkable
from typing import Self

@runtime_checkable
class Hand(CardList):
    def __init__(self) -> None:
        self.__card_list:list[Card] = []

    @property
    def card_list(self):
        return self.__card_list
    
    def cards_left(self)->int:
        return len(self.card_list)
    
    def pop_card(self)->Card:
        top_card = self.__card_list.pop()
        return top_card

    def add_card(self,card:Card)->Self:
        self.__card_list.append(card)
        return self

from .Card import Card
from typing import Self

class Hand():
    def __init__(self) -> None:
        self.__card_list:list[Card] = []

    @property
    def card_list(self)->list[Card]:
        return self.__card_list
    
    def cards_left(self)->int:
        return len(self.__card_list)
    
    def pop_card(self)->Card:
        top_card = self.__card_list.pop(0)
        return top_card

    def add_card(self,card:Card)->Self:
        self.__card_list.append(card)
        return self

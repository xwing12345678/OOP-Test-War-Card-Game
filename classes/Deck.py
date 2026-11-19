from typing import Self
from .Card import Card
from random import randint,randrange,random

class Deck():
    def __init__(self) -> None:
        card_list = []
        for suit in Card.SUITS:
            for rank in Card.VALID_RANKS:
                next_card = Card(suit,rank)
                card_list.append(next_card)
        self.__card_list = card_list

    @property
    def card_list(self):
        return self.__card_list

    def shuffle_deck(self)->Self:
        num = len(self.card_list)
        for card_index_1 in range(num):
            card_index_2 = randint(0, card_index_1)
            self.card_list[card_index_1], self.card_list[card_index_2] = self.card_list[card_index_2], self.card_list[card_index_1]
        return self

    def thousand_shuffle(self)->Self:
        for i in range(0,1000):
            self.shuffle_deck()
        return self

        

    

    

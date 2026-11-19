from typing import Self
from .Card import Card
from .Player import Player
from random import randint,randrange,random
from .Card_list_Protocol import CardList,runtime_checkable

class Deck(CardList):
    def __init__(self) -> None:
        card_list:list[Card] = []
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
            while  card_index_1 == card_index_2:
                card_index_2 = randint(0, card_index_1)
            self.card_list[card_index_1], self.card_list[card_index_2] = self.card_list[card_index_2], self.card_list[card_index_1]
        return self

    def thousand_shuffle(self)->Self:
        for i in range(0,1000):
            self.shuffle_deck()
        return self

    def cards_left(self)->int:
        return len(self.card_list)
    
    def pop_card(self)->Card:
        top_card = self.__card_list.pop(0)
        return top_card

    def deal_all(self,player_list:list[Player])->Self:
        while len(self.__card_list) > 0:
            for player in player_list:
                player.hand.add_card(self.pop_card())
                if len(self.__card_list) <= 0:
                    break
        return self
            
        


        

    

    

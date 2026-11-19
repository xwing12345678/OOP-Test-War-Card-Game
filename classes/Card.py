from typing import Literal,Sequence,Self
from Validations.string_validations import in_literal_list
from Validations.number_validations import int_in_list
suits  = Literal ['H' ,'D', 'S', 'C']

class Card():
    VALID_SUITS  = Literal ['H' ,'D', 'S', 'C']
    SUITS:Sequence[VALID_SUITS]  = ['H' ,'D', 'S', 'C']
    VALID_RANKS = [number for number in range(2,15)]
    def __init__(self,suit:VALID_SUITS,rank:int) -> None:
        self.__rank = rank
        self.__suit = suit
    
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self,rank:int):
        if not int_in_list(rank,self.VALID_RANKS):
            raise ValueError("You can only create a card with a rank of 1 to 14!")
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self,suit:VALID_SUITS):
        if not in_literal_list(suit,self.SUITS):
            raise ValueError("You can only create a suit from: 'H' ,'D', 'S', 'C'!")
        self.__suit = suit
    
    def get_symbol(self)->str:
        if self.__suit == 'H':
            return '♥'
        elif self.__suit == 'D':
            return '♦'
        elif self.__suit == 'S':
            return '♠'
        else:
            return '♣'
    
    def display_card(self)->str:
        return f'{self.__rank} {self.get_symbol()} '


    


    
        

from classes.Card import Card
from classes.Deck import Deck
from classes.Player import Player
from classes.Hand import Hand
from typing import Self

class Game():
    def __init__(self,player:Player) -> None:
        self.__deck = Deck()
        self.__player = player
        self.__computer = Player("Computer")

    def setup_game(self)->Self:
        self.__deck.thousand_shuffle()
        self.__deck.deal_all([self.__computer,self.__player])
        return self

    def winning_player(self,player1:Player,player2:Player)->str|None:
        player1_card = player1.hand.pop_card()
        player2_card = player2.hand.pop_card()
        print(f'''• ========== TURN ==========
                    • Player: {player1_card}
                    • Computer:{player2_card}''')
        if player1_card.rank > player2_card.rank:
            return player1.name
        elif player2_card.rank > player1_card.rank:
                return player2.name
        else:
            return None
                
            
    def play_round(self):
        result = self.winning_player(self.__player,self.__computer)
        if result == None:
            print("• It's a draw! ")
        else:
            print(f'{result} won the round! ')
        print(self.__player.cards_left())
        print(self.__computer.cards_left())
    
from .Hand import Hand


class Player():
    def __init__(self,name:str) -> None:
        self.__name = name
        self.__hand = Hand()

    @property
    def name(self):
        return self.__name
    @property
    def hand(self):
        return self.__hand

    def cards_left(self)->int:
        return len(self.__hand.card_list)

    

    
        
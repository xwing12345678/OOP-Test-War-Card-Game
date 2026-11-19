from classes.Card import Card
from classes.Deck import Deck

new_deck = Deck()

new_deck.shuffle_deck()

shuffled_card_list = new_deck.card_list


for card in shuffled_card_list:
    print(card.display_card())
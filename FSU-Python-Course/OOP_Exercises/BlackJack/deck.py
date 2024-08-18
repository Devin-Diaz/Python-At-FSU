# deck.py

'''
Creating a deck instance, makes a list with all 52 type cards, and randomizes them.
_build_deck() - private function that does cartesian product on suits and values.
deal_card() - retrieves random card from deck, removes it, and returns the card that was removed.
shuffle() - randomize all 52 instances in the list.
reset() - deck is recreated with 52 instances and shuffled
__iter__ - iterable instance.
__len__ - can check length via len() of the object since it's iterable
__str__ - check all cards in deck
'''

from card import Card
import random

class Deck:
    def __init__(self) -> None:
        self._suits = ['♣', '♦', '♥', '♠']
        self._values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 
                  'Jack', 'Queen', 'King', 'Ace']

        self._deck = []
        self._build_deck()
        self.shuffle()

    def _build_deck(self) -> list[Card]:
        self._deck = [Card(value, suit) for value in self._values for suit in self._suits]

    def deal_card(self) -> Card:
        random_card = random.choice(self._deck)
        self._deck.remove(random_card)
        return random_card        

    def shuffle(self) -> None:
        random.shuffle(self._deck)
    
    def reset(self) -> None:
        self._build_deck()
        self.shuffle()
    
    def __iter__(self) -> None:
        return iter(self._deck)

    def __len__(self) -> int:
        return len(self._deck)

    def __str__(self) -> str:
        return ', '.join(str(card) for card in self._deck)

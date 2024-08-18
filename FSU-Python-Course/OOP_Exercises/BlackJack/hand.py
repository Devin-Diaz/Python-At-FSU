# hand.py

'''
When an instance of hand is made, empty list of type card is created.
add_card() - adds card to list attribute of hand.
parse_values() - receives Card instance, and accesses value attribute to return the points of the card.
total_value() - checks the total value of a hand.
is_valid() - boolean function that chekcs whether or not hand is valid 
__iter__ - and iterable object.
__str__ - to string function to display entire hand.
'''

from card import Card

class Hand:
    def __init__(self) -> None:
        self._hand = []

    def add_card(self, card: Card):
        self._hand.append(card)
        return card
    
    def parse_value(self, card: Card):
        if card.value == 'King' or card.value == 'Queen' or card.value == 'Jack': return 10
        else: return int(card.value)

    def total_value(self):
        total = 0
        ace_counter = 0
        for card in self._hand:
            if card.value == 'Ace': 
                ace_counter += 1
                continue
            total += self.parse_value(card)
        
        for _ in range(ace_counter):
            if total + 11 <= 21: total += 11
            else: total += 1
        return total
    
    def is_valid(self):
        return self.total_value() <= 21
    
    def __iter__(self):
        return iter(self._hand)
    
    def __str__(self):
        return ', '.join(str(card) for card in self._hand)

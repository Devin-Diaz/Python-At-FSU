# card.py

'''
Card object with value and suit fields. Reads as, 'value of suit'.
__str__ - returns data of card
'''

class Card:
    def __init__(self, value: str, suit: str) -> None:
        self.value = value
        self.suit = suit
    
    def __str__(self) -> str:
        return f'{self.value} of {self.suit}'


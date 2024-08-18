# dealer.py

'''
'''
from player import Player
from hand import Hand

class Dealer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.hand = Hand()
        self.is_standing = False
        self.busted = False
    
    def stand(self) -> None:
        return super().stand()

    def winning_state(self) -> None:
        if self.hand.total_value() >= 17:
            self.stand()
        if not self.hand.is_valid():
            self.busted = True
            return False
        return True
    
    def in_game_hand(self):
        return (f"Dealer 🤝\n"
        f"Hand: {self.hand._hand[0]}, [hidden] \n"
        f"Standing: {self.is_standing} | Busted: {self.busted}\n")
    
    def __str__(self) -> str:
        return (f"Dealer 🤝\n"
        f"Hand: {self.hand} = {self.hand.total_value()} points\n"
        f"Standing: {self.is_standing} | Busted: {self.busted}\n")
# player.py

'''
Instance of a player, when created assigned an id, empty hand, and flags that check whether they
are standing or busted. 
stand() - when function is called, player is set to a standing state.
winning_state() - checks if a player currently has a valid hand, if not there standing and busted state gets flipped.
reset() - If player chooses to play again they start with default stats again.
__str__ - displays player id, their current hand, and states
'''

from hand import Hand

class Player:
    player_id_static = 0
    def __init__(self) -> None:
        Player.player_id_static += 1
        self.id = Player.player_id_static
        self.hand = Hand()
        self.is_standing = False
        self.busted = False
        self.money = 0

    def stand(self) -> None:
        self.is_standing = True
    
    def winning_state(self) -> None:
        if not self.hand.is_valid():
            self.stand()
            self.busted = True
            return False
        return True
    
    def reset(self):
        self.is_standing = False
        self.busted = False
        self.hand = Hand()
    
    def display_bet(self):
        return f'player {self.id} placed ${self.money}'
    
    def __str__(self) -> str:
        return (f"Name: player {self.id}\n"
        f"Hand: {self.hand} = {self.hand.total_value()} points\n"
        f"Standing: {self.is_standing} | Busted: {self.busted}\n"
        f"Bet: ${self.money}\n")
 



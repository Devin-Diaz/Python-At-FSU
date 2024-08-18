# all_players.py

'''
Creates an iterable instance of type Player.
add() - adds player to the instance.
remove_loser() - player is removed if their hand is no longer valid.
__iter__ - makes all players object iterable.
__str__ - displays all players who still have a chance of winning.
'''

from player import Player

class AllPlayers:
    def __init__(self) -> None:
        self._all_players = []

    def add(self, player: Player) -> None:
        self._all_players.append(player)
    
    def remove(self, player: Player) -> None:
        self._all_players.remove(player)

    def reset(self):
        self._all_players = []

    def __iter__(self) -> None:
        return iter(self._all_players)
    
    def __len__(self) -> int:
        return len(self._all_players)
    
    def __str__(self) -> str:
        return '\n\n'.join(str(player) for player in self._all_players)


# game_round.py

from deck import Deck
from player import Player
from all_players import AllPlayers
from dealer import Dealer

def play_blackjack():
    deck = Deck()
    all_players = AllPlayers()
    dealer = Dealer()

    def total_players() -> int:
        total = int(input('\nEnter total players: '))
        return total

    def create_players(total: int, all_players: AllPlayers):
        Player.player_id_static = 0  
        for _ in range(total):
            all_players.add(Player())

    def place_bets(all_players: AllPlayers) -> None:
        print('\nBets will now be placed.')
        for player in all_players:
            bet = int(input(f'player {player.id}, enter bet amount [$2 - $500]: '))
            player.money = bet

    def deal_initial_cards(all_players: AllPlayers, dealer: Dealer, deck: Deck):
        print('\nCards will now be dealt.')
        for player in all_players:
            player.hand.add_card(deck.deal_card())
            player.hand.add_card(deck.deal_card())

        dealer.hand.add_card(deck.deal_card())
        dealer.hand.add_card(deck.deal_card())

    def show_players_and_dealer(all_players: AllPlayers, dealer: Dealer):
        print(dealer.in_game_hand())
        for player in all_players:
            print(player)

    def black_jack_all(all_players: AllPlayers):
        for player in all_players:
            if player.hand.total_value() == 21:
                player.money *= 1.5
                print(f'**Blackjack for player {player.id}!** +${player.money}\n')
                all_players.remove(player)

    def black_jack(player: Player, all_players: AllPlayers):
        if player.hand.total_value() == 21:
            player.money *= 1.5
            print(f'**Blackjack for player {player.id}!** +${player.money}\n')
            all_players.remove(player)

    def all_players_standing(all_players: AllPlayers) -> bool:
        for player in all_players:
            if not player.is_standing:
                return False
        return True

    def no_players_competing(all_players: AllPlayers) -> bool:
        return len(all_players) == 0

    def hit_or_stand(all_players: AllPlayers, deck: Deck):
        while True:
            if no_players_competing(all_players): 
                print('All players are out.')
                break

            if all_players_standing(all_players): 
                print('All players standing.')
                break
            
            for player in all_players:
                if player.is_standing: continue
                user_ans = input(f'player {player.id}, hit or stand (H / S): ')
                if user_ans.upper() == 'H':
                    player.hand.add_card(deck.deal_card())
                    print(player)
                    black_jack(player, all_players)
                    if not player.winning_state():
                        all_players.remove(player)
                        print('BUSTED!\n')
                else:
                    player.stand()
                    print('STAND\n')

    def dealer_play(dealer: Dealer, deck: Deck):
        while dealer.hand.total_value() < 17:
            dealer.hand.add_card(deck.deal_card())
            print('Dealer HITS')
            print(dealer)
        
        if dealer.hand.total_value() > 21:
            dealer.busted = True
            print('Dealer BUSTED!')

    def players_lose_bet(all_players: AllPlayers):
        for player in all_players:
            player.money = 0

    def round_summary(all_players: AllPlayers, dealer: Dealer):
        if not dealer.winning_state():
            print('Dealer Lost!\n')
            for player in all_players:
                winnings = player.money * 3  # 3x payout if player beats the dealer
                print(f'Player {player.id} wins with $+{winnings}')
                player.money = winnings
        
        elif dealer.winning_state() and no_players_competing(all_players):
            print(f'\nDealer Won!')
            print(dealer)
            players_lose_bet(all_players)
        else:
            for player in all_players:
                if player.hand.total_value() > dealer.hand.total_value() and not player.busted:
                    winnings = player.money * 3  # 3x payout if player beats the dealer
                    print(f'Player {player.id} wins with $+{winnings}')
                    player.money = winnings
                elif player.hand.total_value() == dealer.hand.total_value():
                    print(f'Player {player.id} ties with the dealer and keeps their bet of ${player.money}')
                else:
                    print(f'Player {player.id} loses')
                    player.money = 0

    while True:
        total = total_players()
        create_players(total, all_players)
        place_bets(all_players)
        deal_initial_cards(all_players, dealer, deck)
        show_players_and_dealer(all_players, dealer)
        black_jack_all(all_players)
        hit_or_stand(all_players, deck)
        
        if all_players_standing(all_players):
            dealer_play(dealer, deck)
        
        round_summary(all_players, dealer)
        
        dealer.reset()
        all_players.reset()
        deck.reset()

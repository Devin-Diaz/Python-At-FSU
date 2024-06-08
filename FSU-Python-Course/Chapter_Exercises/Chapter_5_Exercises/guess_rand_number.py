import random

def generate_random_num() -> int:
    return random.randint(0, 100)

def higher_or_lower(target_num: int, input_num: int) -> str:
    if input_num < target_num: print('too low!')
    elif input_num > target_num: print('too high!')

def guessing_game() -> None:
    random_num = generate_random_num()
    user_guess = int(input('Guess the random # (1-100): '))

    while user_guess != random_num:
        higher_or_lower(random_num, user_guess)
        user_guess = int(input('Guess the random # (1-100): '))

    print(f'CORRECT! The random number was {random_num}!')

def main() -> None:
    game_state = True
    while game_state:
        guessing_game()
        user_ans = input('Do you want to play agan? (y/n): ')
        if(user_ans.lower() == 'y'): 
            print("Let's play again!")
            continue
        else: 
            print('thanks for playing!')
            game_state = False

main()
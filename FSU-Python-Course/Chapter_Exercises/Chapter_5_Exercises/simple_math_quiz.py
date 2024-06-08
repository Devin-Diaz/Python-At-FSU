import random

def random_number_sum(x: int, y: int) -> int:
    return x + y

def generate_two_random_numbers() -> list[int]:
    return [int(random.random() * 100), int(random.random() * 100)]

def math_quiz() -> None:
    nums = generate_two_random_numbers()
    x, y = nums[0], nums[1]
    user_ans = int(input(f'Sum the following numbers, {x} + {y}: '))

    if user_ans == random_number_sum(x, y): print('CORRECT!')
    else: print('INCORRECT!')

math_quiz()


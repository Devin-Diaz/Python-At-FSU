import random

def even_or_odd(num: int) -> str:
    if num % 2 == 0: return 'is even'
    else: return 'is odd'

def generate_hundred_random_nums() -> list[int]:
    output = []
    for i in range(100):
        output.append(int(random.random() * 100))
    return output

def main() -> None:
    nums = generate_hundred_random_nums()
    for n in nums:
        print(f' {n} {even_or_odd(n)}')

main()
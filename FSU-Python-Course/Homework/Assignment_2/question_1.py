'''
Write a program that lets the user enter a positive integer (greater than zero) and then uses a loop
to calculate the factorial of that number. Display the factorial. Perform input validation using a loop.
'''

# Gets and returns user input and ensures input is greater than 0
def user_input() -> int:
    user_ans = int(input('Enter number: '))

    while user_ans <= 0:
        user_ans = int(input('Enter number: '))
    
    return user_ans

# Calculates the factorial of the input positive integer iteratively and returns the result
def factorial(num: int) -> int:
    ans = 1
    for i in range(1, num + 1):
        ans *= i
    
    return ans

# Recieves user input, does calculation, and prints out result of the factorial
def calc_factorial() -> None:
    num = user_input()
    ans = factorial(num)
    print(f'The factorial of {num}! is: {ans}')

# Begins program
calc_factorial()
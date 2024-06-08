'''
Write a program that uses nested loops to draw the following pattern. The number of rows should
be input by the user.
'''

# Receives user input and ensures rows are not negative, returns number of rows
def user_input() -> int:
    user_ans = int(input('Enter number of rows: '))

    while user_ans < 0:
        user_ans = int(input('Enter number of rows: '))
    
    return user_ans

# Nested loops that create the stair case via '#' symbol and empty prefix string for spacing between symbols
def create_stairs(rows: int, prefix: str = '') -> None:
    for i in range(rows):
        print('#', end='')
        for j in range(i):
            prefix += ' '
            print(prefix, end='')
            break 
        print('#\n', end = '')

# Recieves user input and prints our rows of the stair case
def stair_program() -> None:
    user_ans = user_input()
    create_stairs(user_ans)

# Begins program
stair_program()
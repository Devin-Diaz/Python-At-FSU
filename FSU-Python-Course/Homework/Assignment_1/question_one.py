'''
Create a change-counting game that gets the user to enter the number of coins required to make
exactly one dollar. The program should prompt the user to enter the number of pennies, nickels,
dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program
should congratulate the user for winning the game. Otherwise, the program should display a
message indicating whether the amount entered was more than or less than one dollar
'''

# constant variable denoting what value a user must reach to win the change counting game
ONE_DOLLAR = 1.00

# recieves user input for total count of each denomination and does conversions for it's value. Returns the sum of the values of all denominations
def calculate_denominations():
    penny_input = int(input('Enter number of pennie(s): '))
    nickel_input = int(input('Enter number of nickel(s): '))
    dime_input = int(input('Enter number of dime(s): '))
    quarter_input = int(input('Enter number of quarter(s): '))

    penny_total = penny_input * 0.01
    nickel_total = nickel_input * 0.05
    dime_total = dime_input * 0.1
    quarter_total = quarter_input * 0.25

    total_change = (penny_total, nickel_total, dime_total, quarter_total)
    return round(sum(total_change), 2)

# takes value of the summed values of the denonminations and determines whether the user is at exactly one dollar, under, or over
def result(input: float):
    if(input == ONE_DOLLAR): print('Congrats, you win!')
    elif(input > ONE_DOLLAR): print(f'The amount entered: ${input} is greater than ${ONE_DOLLAR}, you lose!')
    else: print(f'The amount entered: ${input}, is less than ${ONE_DOLLAR}, you lose!')

# recieves the summed values of denominations and calculates the result of the user based on their input
def change_counting_game():
    user_input = calculate_denominations()
    result(user_input)

# begins program
change_counting_game()

    





    

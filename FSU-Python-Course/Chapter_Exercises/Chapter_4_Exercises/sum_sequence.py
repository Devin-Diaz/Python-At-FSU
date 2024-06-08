'''
Write a program with a loop that asks the user to enter a series of positive numbers. The user
should enter a negative number to signal the end of the series. After all the positive numbers have
been entered, the program should display their sum
'''

def seperateLineInputs():
    user_input = 0
    total = 0

    while user_input >= 0:
        total += user_input
        user_input = int(input('Enter # (-# to quit): '))
    print(total)    


def sameLineInput():
    user_input = input('Enter all numbers seperated by a space (-# to terminate seq): ')
    input_to_arr = user_input.split(' ')
    input_to_arr.pop()
    total = 0

    for n in input_to_arr:
        total += int(n)
    
    print(total)
    

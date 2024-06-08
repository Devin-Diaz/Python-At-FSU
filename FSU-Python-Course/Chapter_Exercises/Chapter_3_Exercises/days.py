'''
Write a program that asks the user for a number in the range of 1 through 7. The program should
display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 =
Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display an error message if
the user enters a number that is outside the range of 1 through 7.
'''

def whichDay(input):
    if input == 1:
        print('Monday')
    elif input == 2:
        print('Tuesday')
    elif input == 3:
        print('Wednesday')
    elif input == 4:
        print('Thursday')
    elif input == 5:
        print('Friday')
    elif input == 6:
        print('Saturday')
    elif input == 7:
        print('Sunday')

def daysProgram():
    userAns = int(input('Enter a number (1-7) inclusive: '))

    while userAns < 1 or userAns > 7:
        print('ERROR, NUMBER IS NOT BETWEEN 1-7')
        userAns = int(input('Enter a number (1-7) inclusive: '))

    whichDay(userAns)

daysProgram()



'''
On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as
follows:

Pocket 0 is green.
For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
pockets are black.
For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
pockets are red.
For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
pockets are black.
For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
pockets are red.

Write a program that asks the user to enter a pocket number and displays whether the pocket is
green, red, or black. The program should display an error message if the user enters a number that
is outside the range of 0 through 36.
'''

def getColor(id, inputNum):
    if id == 1:
        print('black' if evenOrOdd(inputNum) else 'red')
    elif id == 2:
        print('red' if evenOrOdd(inputNum) else 'black')
    elif id == 3:
        print('black' if evenOrOdd(inputNum) else 'red')
    elif id == 4:
        print('red' if evenOrOdd(inputNum) else 'black')


def evenOrOdd(inputNum):
    return inputNum % 2 == 0


def calculateColor(inputNum):
    if inputNum == 0: 
        print('Green')
    elif 1 <= inputNum <= 10: 
        getColor(1, inputNum)
    elif 11 <= inputNum <= 18: 
        getColor(2, inputNum)
    elif 19 <= inputNum <= 28: 
        getColor(3, inputNum)
    else: 
        getColor(4, inputNum)


def startProgram():
    #Scanner
    userAns = int(input('Enter pocket number (0 - 36) inclusive: '))

    # while loop to check that is between 0-36
    while(userAns < 1 or userAns > 36):
        print('*ERROR* pocket # is not within constraints. Try again.')
        userAns = int(input('Enter pocket number (0 - 36) inclusive: '))

    print(f'Pocket color for #{userAns} is: ', end="")
    calculateColor(userAns)




# here
startProgram()

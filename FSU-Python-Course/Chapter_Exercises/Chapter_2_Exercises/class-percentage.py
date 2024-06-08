'''
Write a program that asks the user for the number of males and the number of females registered in
a class. The program should display the percentage of males and females in the class
'''

totalMales = float(input('Enter total males in class: '))
totalFemales = float(input('Enter total females in class: '))

malePercentage = (totalMales / (totalMales + totalFemales)) * 100
femalePercentage = 100.00 - malePercentage

print(f'''
Class percentages:
Male percentage: {malePercentage:.2f}%
Female percentage: {femalePercentage:.2f}%
''')
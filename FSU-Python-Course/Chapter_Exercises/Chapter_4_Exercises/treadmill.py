'''
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop
to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
'''

CAL_PER_MIN = 4.2
total_cals_burned = 0

for i in range(1, 31):
    total_cals_burned += CAL_PER_MIN

    if(i == 10): print(f'Cals burned at 10 mins: {int(total_cals_burned)}')
    if(i == 15): print(f'Cals burned at 15 mins: {int(total_cals_burned)}')
    if(i == 20): print(f'Cals burned at 20 mins: {int(total_cals_burned)}')
    if(i == 25): print(f'Cals burned at 25 mins: {int(total_cals_burned)}')
    if(i == 30): print(f'Cals burned at 30 mins: {int(total_cals_burned)}')


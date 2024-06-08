'''
Write a program that calculates and displays a person's body mass index (BMI). The BMI is often
used to determine whether a person is overweight or underweight for his or her height. A person's
BMI is calculated with the following formula: BMI = weight * 703 / height^2

where weight is measured in pounds and height is measured in inches. The program should ask the
user to enter his or her weight and height, then display the user's BMI. The program should also
display a message indicating whether the person has optimal weight, is underweight, or is
overweight. A person's weight is considered to be optimal if his or her BMI is between 18.5 and 25.
If the BMI is less than 18.5, the person is considered to be underweight. If the BMI value is greater
than 25, the person is considered to be overweight.
'''
# constant variables that will determine whether the users weight is healthy or not
OPTIMAL_LOW = 18.5
OPTIMAL_HIGH = 25

# displays the results of the program based off the user's calculated BMI
def determine_results(bmi: float):
    if OPTIMAL_LOW <= bmi <= OPTIMAL_HIGH: print('optimal weight.')
    elif bmi < OPTIMAL_LOW: print('underweight')
    else: print('overweight')

# calculates the user's BMI based off their inputted weight in pounds and height in inches
def calculate_bmi(weight, height):
    return weight * 703 / pow(height, 2)

# collects user's height and weight and returns their calculated BMI
def get_user_input():
    user_weight = int(input('Enter weight (lbs): '))
    user_height = int(input('Enter height (inches): '))
    return calculate_bmi(user_weight, user_height)

# collects user's BMI and determines the results 
def bmi_program():
    user_bmi = get_user_input()
    determine_results(user_bmi)

# begins program
bmi_program()

'''
Write a program that writes a series of random numbers to a file. Each random number should be in
the range of 1 through 500. The application should let the user specify how many random numbers
the file will hold
'''
import random

# 'a' - append to existing file, 'w' - overwrites all existing contents in file, 'x' - creates new file, error if already exists. 
def write_random_nums_to_file():
    user_ans = int(input('How many random nums do you to generate: '))
    with open("Tester_Text_Files/random_nums.txt", "a") as file:
        for _ in range(user_ans):
            random_num = random.randint(1, 500)
            file.write(f'{random_num}\n')

write_random_nums_to_file()
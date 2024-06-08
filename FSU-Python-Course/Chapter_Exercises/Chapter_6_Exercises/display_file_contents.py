'''
Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
Write a program that displays all of the numbers in the file.
'''

# reads as, with open function, open this file as variable file, then read it's contents. 
with open("Tester_Text_Files/numbers.txt", "r") as file:
    print(file.read())


'''
Write a program that asks the user for the name of a file. The program should display only the first
five lines of the file's contents. If the file contains less than five lines, it should display the file’s
entire contents
'''

# strip() function removes any whitespace characters from both ends of the string including new line characters. 




def get_user_input():
    user_ans = input('Enter file name: ')
    return user_ans

def readFile():
    file_name = get_user_input()
    file_path = f'Tester_Text_Files/{file_name}'

    with open(file_path, "r") as file:
        for _ in range(5):
            print(file.readline().strip())

readFile()



'''
Write a program that asks the user for his or her name, then asks the user to enter a sentence that
describes himself or herself. Once the user has entered the requested input, the program should
create an HTML file, containing the input, for a simple Web page.
6. Modify the program that you wrote for Question 3 so it handles the following exceptions:
 It should handle any IOError exceptions that are raised when the file is opened and data is
read from it.
 It should handle any ValueError exceptions that are raised when the items that are read
from the file are converted to a number.
'''

def user_input():
    ans = input('Enter requested sentence: ')
    return ans

def generate_html_file():
    user_sentence = user_input()

    with open('Tester_Text_Files/index.html', "x") as file:
        file.write(f'<h1>{user_sentence}</h1>')

generate_html_file()
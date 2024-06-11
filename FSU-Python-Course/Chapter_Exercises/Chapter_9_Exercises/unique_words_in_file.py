'''
Write a program that opens a specified text file, and then displays a list of all the unique 
words found in the file. Hint: Store each word as an element of a set.
'''

import re

def user_input():
    ans = input('Enter File Path: ')
    return ans

def remove_alpha_numeric(line: str) -> str:
    new_line = re.sub('[^a-zA-Z ]', '', line)
    return new_line

def display_set(hashset: set[str]):
    for i, n in enumerate(hashset):
        print(f'{i}:  {n}')

def parse_data() -> set[str]:
    hashset = set()
    try:
        file_path = user_input()
        with open(file_path, "r") as file:
            for line in file:
                new_line = remove_alpha_numeric(line.strip())
                parsed_line = new_line.split()
                for word in parsed_line:
                    hashset.add(word)
    except FileNotFoundError:
        print('File not found.')
        return 0

    return hashset

def all_unique_words() -> None:
    unique_words = parse_data()
    display_set(unique_words)

all_unique_words()
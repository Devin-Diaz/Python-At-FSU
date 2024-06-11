'''
Write a program that reads the contents of a text file. The program should create a dictionary in which the 
keys are the individual words found in the file and the values are the number of times each word appears. For 
example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key 
and 128 as the value. The program should display the words and the frequency of each word.
'''

import re

def display_dict(hashmap: dict) -> None:
    print(f'{"Word":<20} Counter')
    print('-' * 30)
    for k, v in hashmap.items():
        print(f'{k:<20} {v}')

def remove_alpha_numeric(line: str) -> str:
    new_line = re.sub('[^a-zA-Z0-9 ]', '', line)
    return new_line

def parse_file() -> dict:
    hashmap = dict()

    try:
        with open("tester_files/random_text.txt", "r") as file:
            for line in file:
                new_line = remove_alpha_numeric(line.strip())
                parsed_line = new_line.split()
                for word in parsed_line:
                    hashmap[word] = 1 + hashmap.get(word, 0)

    except FileNotFoundError:
        print('File not found.')
        return {}
    
    return hashmap

def count_word_occurrence() -> None:
    data = parse_file()
    display_dict(data)

count_word_occurrence()
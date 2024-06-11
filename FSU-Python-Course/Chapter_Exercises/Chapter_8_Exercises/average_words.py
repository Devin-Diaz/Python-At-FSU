'''
Write a program that opens a specified text file, and then displays a list of all the unique words found in the file. 
Hint: Store each word as an element of a set.
'''

import re

# Removes all characters from a string that are not letters, digits, or spaces.
def remove_alpha_numeric(line: str) -> str:
    new_line = re.sub('[^a-zA-Z ]', '', line)
    return new_line

# parses text file of sentences. Returns a list where first element is total lines of file and second is list of words each sentence
def parse_file() -> list[int, list]:
    total_lines = 0
    len_of_sentence = []
    with open("words.txt", "r") as file:
       for line in file:
            total_lines += 1
            new_line = remove_alpha_numeric(line.strip())
            parsed_line = new_line.split()
            word_total = len(parsed_line)
            len_of_sentence.append(word_total)

    return [total_lines, len_of_sentence]

def find_average() -> None:
    data = parse_file()
    sum_of_elements = sum(data[1])
    total_sentences = data[0]
    if total_sentences > 0:
        print(f'Average words per sentence: {sum_of_elements // total_sentences}')
    else:
        print('No sentences found.')

find_average()

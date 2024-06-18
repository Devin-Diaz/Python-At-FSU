'''
Write a program that reads the contents of two text files and compares them in the following ways:
    It should display a list of all the unique words contained in both files.
    It should display a list of the words that appear in both files.
    It should display a list of the words that appear in the first file but not the second.
    It should display a list of the words that appear in the second file but not the first.
    It should display a list of the words that appear in either the first or second file, but not both.
'''
import re

# removes all alpha-numeric chars from a line
def clean_up_line(line: str) -> str:
    new_line = re.sub("[^a-zA-Z0-9 ]", '', line)
    return new_line

# gets file path of file we want to read
def get_file_path() -> str:
    ans = input('Enter file path: ')
    return ans

# returns a set of all the contents in the text file
def parse_file_data() -> set:
    res = set()
    try:
        file_path = get_file_path()
        with open(file_path, "r") as file:
            for line in file:
                clean_line = clean_up_line(line.strip())
                parsed_line = clean_line.split()
                for word in parsed_line:
                    res.add(word)
    except FileNotFoundError:
        print(f'File at {file_path} does not exist.')
        return set()
    return res

# parse x amount of files, data will be stored in a list of sets.
def parse_all_files() -> list[set]:
    all_data = []
    for i in range(2):
        file_data = parse_file_data()
        all_data.append(file_data)
    return all_data

def unique_words_in_files(all_data_set: list[set]) -> None:
    for cur_set in all_data_set:
        print('Unique words in file:')
        for word in cur_set:
            print(word, end=' ')
        print('\n')

def intersection_in_files(all_data_sets: list[set]) -> None:
    set_1 = all_data_sets[0]
    set_2 = all_data_sets[1]
    res_set = set_1.intersection(set_2)
    print(f'Intersection of files: {res_set}\n')

def difference_of_files(all_data_sets: list[set]) -> None:
    set_1 = all_data_sets[0]
    set_2 = all_data_sets[1]
    res_set_1 = set_1.difference(set_2)
    res_set_2 = set_2.difference(set_1)
    print('Difference of both files:')
    print(res_set_1)
    print(res_set_2,'\n')

def symmetric_difference(all_data_sets: list[set]) -> None:
    set_1 = all_data_sets[0]
    set_2 = all_data_sets[1]

    union_set = set_1.union(set_2)
    inter_set = set_1.intersection(set_2)
    symmetric_diff_set = union_set.difference(inter_set)
    print(f'Symmetric difference set: {symmetric_diff_set}')


def compare_files():
    all_data = parse_all_files()
    unique_words_in_files(all_data)
    intersection_in_files(all_data)
    difference_of_files(all_data)
    symmetric_difference(all_data)

compare_files()
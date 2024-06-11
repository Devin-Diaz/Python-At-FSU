'''
Write a program that reads the contents of two text files and compares them in the following ways:
    It should display a list of all the unique words contained in both files.
    It should display a list of the words that appear in both files. 
    It should display a list of the words that appear in the first file but not the second. 
    It should display a list of the words that appear in the second file but not the first.
    It should display a list of the words that appear in either the first or second file, but not both.
'''

import unique_words_in_file as my_funcs

def get_data_from_files() -> list[set]:
    data = []

    files_to_be_checked = int(input('How many files are you checking?: '))

    for i in range(files_to_be_checked):
        unique_words = my_funcs.parse_data()
        data.append(unique_words)
    
    return data


print(get_data_from_files())
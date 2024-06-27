'''
Word Index

Write a program that reads the contents of a text file. The program should create a dictionary in which
the key-value pairs are described as follows:
    
    Key: The keys are the individual words found in the file.
    Values: Each value is a list or a set that contains the line numbers in the file where the word
    (the key) is found.

For example, suppose the word “robot” is found in lines 7, 18, 94, and 138. The dictionary would contain
an element in which the key was the string “robot”, and the value was a list or a set containing the
numbers 7, 18, 94, and 138.

Once the dictionary is built, the program should create another text file, known as a word index, listing
the contents of the dictionary. The word index file should contain a listing of the words that are stored
as keys in the dictionary, along with the line numbers where the words appear in the original file.
'''

# Gets path to file we will parse
def get_file_path() -> None:
    path = input('Enter file path: ')
    return path

# opens file specified by user input and parses file by storing words and line location in the file via dictionary
def read_parse_file() -> dict:
    word_tracker = dict()
    line_counter = 1
    try:
        file_path = get_file_path()
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = line.split()
                for word in parsed_line:
                    if word not in word_tracker:
                        word_tracker[word] = set()
                    word_tracker.get(word).add(line_counter)
                line_counter += 1 
    except FileNotFoundError:
        print(f'File with path: {file_path} not found.')
        return None

    return word_tracker

# writes word_tracker dictionary data in a nicely formatted text document called output
def write_data_to_file(word_tracker: dict) -> None:
    with open("output.txt", "w") as file:
        for key, val in word_tracker.items():
            sorted_values = sorted(val)
            values = ' '.join(map(str, sorted_values))
            data = f'{key}: {values}\n'
            file.write(data)

# reads a file, then after finds which line it appears in the text file. Writes it to a new file in neat format
def word_index_program() -> None:
    file_data = read_parse_file()
    write_data_to_file(file_data)
    print('Data has been written successfully.')

# begins program
word_index_program()

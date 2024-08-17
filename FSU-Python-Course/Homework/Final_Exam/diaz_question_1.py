'''
Write a program that lets the user enter a string and displays the character that appears most
frequently in the string. If several characters have the same highest frequency, display the first
character with that frequency. The program need not be case sensitive.
'''

# finds most frequent character via map and it's values
def most_freq_char(word: str) -> str:
    fixed_word = word.upper()
    hashmap = dict()
    for c in fixed_word:
        hashmap[c] = 1 + hashmap.get(c, 0)
    
    max_char = max(hashmap, key=hashmap.get)
    return f'The character that appears most frequently in the string is {max_char}.'

# gets user input and finds the max freq
def find_freq_char() -> None:
    ans = input('Enter a string: ')
    print(most_freq_char(ans))

# begins program
find_freq_char()
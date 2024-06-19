'''
Write a program with a function that accepts a string as an argument and returns a copy of the
string with the first character of each sentence capitalized.

For instance, if the argument is “hello. my name is Joe. what is your name?” the function should
return the string “Hello. My name is Joe. What is your name?”

The program should let the user enter a string and then pass it to the function. The modified string
should be displayed.
'''

# receives user string. Ensures that it is at least two characters long
def get_string() -> str:
    ans = input('Enter sentence: ')
    while len(ans) < 2:
        print('Sentence must be at least 2 characters long. Try again.')
        ans = input('Enter sentence: ')
    return ans

# converts input string into list via period delimeter. 
# We then iterate through each sentence adjusting accordingly if it has contents
def capitalize_sentences(text: str) -> str:
    sentences = text.split('. ')
    capitalized_sentences = []

    for sentence in sentences:
        if sentence:
            capitalized_sentence = sentence[0].upper() + sentence[1:]
            capitalized_sentences.append(capitalized_sentence)
        else:
            capitalized_sentences.append(sentence)  # handle empty sentences
    return '. '.join(capitalized_sentences)

# Receives user input and ensures sentences are capitalized at the beginning. 
def convert_first_to_upper() -> None:
    user_ans = get_string()
    output_phrase = capitalize_sentences(user_ans)
    print(f'Result: {output_phrase}')

# start program
convert_first_to_upper()

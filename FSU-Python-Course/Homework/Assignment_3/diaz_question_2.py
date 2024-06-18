'''
The Springfork Amateur Golf Club has a tournament every weekend. The club president has asked
you to write two programs:

    a. A program that will read each player's name and golf score as keyboard input, then save
    these as records in a file named golf.txt. (Each record will have a field for the player's name
    and a field for the player's score.)

    b. A program that reads the records from the golf.txt file and displays them.
'''

# user input for golfer's name and their score
def get_golfer_details() -> list:
    golfer_name = input("Enter golfer's name: ")
    golfer_score = int(input(f"Enter {golfer_name}'s score: "))
    return [golfer_name, golfer_score]

# writes golfer data to specified text file. Each player is written on a new line
def write_golfer_data() -> None:
    with open('golf.txt', 'a') as file:
        golfer_data = get_golfer_details()
        golfer_name = golfer_data[0]
        golfer_score = golfer_data[1]
        file.write(f'Name: {golfer_name} | Score: {golfer_score}\n\n')

# displays all data in console that is written to golf.txt. Consists of players names' and scores.
def read_records() -> None:
    with open('golf.txt', 'r') as file:
        print("\nSpringfork Amateur Golf Club Tournament Records")
        print('-----------------------------------------------')
        print(file.read())

# prompts user with options of reading golfer data, writing golfer data, or quitting the program 
def golf_data() -> None:
    state = True
    while state:
        user_ans = int(input('Write data? (press 1) | Read data? (press 2) | Quit? (press 3)?: '))
        if user_ans == 1:
            user_write = input("Enter golfer data? (y/n): ")
            if user_write == 'y':
                write_golfer_data()
            else:
                print('Script Done.')
                state = False

        elif user_ans == 2:
            read_records()
            
        else:
            print('Script Done.')
            state = False

# begins program 
golf_data()

'''
The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown below. The Lo Shu Magic
Square has the following properties:

- The grid contains the numbers 1 through 9 exactly.
- The sum of each row, each column, and each diagonal all add up to the same number.

In a program you can simulate a magic square using a two-dimensional list. Write a function that
accepts a two-dimensional list as an argument and determines whether the list is a Lo Shu Magic
Square. Test the function in a program. Make your program as modular as possible.
'''

# ensures element is between 1 - 9
def between_one_and_nine(element) -> bool:
    return 1 <= element <= 9

# Verifies that each element is unique within the board 
def is_unique(board: list[list[int]]) -> bool:
    hashset = set()

    for i in range(3):
        for j in range(3):
            current = board[i][j]
            in_constraint = between_one_and_nine(current)

            if current in hashset or not in_constraint: return False
            hashset.add(current)

    return True

# Verifies that all rows, cols, and diagnols have a sum of 15
def sums_to_15(board: list[list[int]]):
    row_sums = [0, 0, 0]
    col_sums = [0, 0, 0]
    diag1_sum = 0
    diag2_sum = 0

    for i in range(3):
        for j in range(3):
            row_sums[i] += board[i][j]
            col_sums[j] += board[i][j]
            if i == j:
                diag1_sum += board[i][j]
            if i + j == 2:
                diag2_sum += board[i][j]
    
    # concats lists and ensures all elements within are equal to 15
    if all(x == 15 for x in row_sums + col_sums + [diag1_sum, diag2_sum]):
        return True
    
    return False

# Checks if our Lo Shu Magic Square is valid
def valid_magic_square(board: list[list[int]]) -> bool:

    if len(board) != 3 or any(len(row) != 3 for row in board):
        return False
    
    unique_board = is_unique(board)
    all_fifteen = sums_to_15(board)

    return unique_board and all_fifteen

board = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 10]
]

print(valid_magic_square(board))






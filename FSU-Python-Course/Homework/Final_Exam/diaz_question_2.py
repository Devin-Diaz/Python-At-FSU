'''
Write a recursive function that accepts an integer argument, n. The function should display n lines of
asterisks on the screen, with the first line showing 1 asterisk, the second line showing 2 asterisks, up
to the nth line which shows n asterisks. Test the function.
'''

# does recursion to build the stair case by appending a new star and line on each method call
def display_lines_helper(n: int, prefix: str):
    if n == 0:
        return ''
    prefix += '*'
    if n == 1:
        return prefix
    return prefix + '\n' + display_lines_helper(n - 1, prefix)

# used for abstraction so the user doesn't have to enter the prefex string
def display_lines(n: int) -> str:
    return display_lines_helper(n, '')

# calls recursion function to build stair case based off user input 
def stair_case() -> None:
    ans = int(input('How many lines to display? '))
    print(display_lines(ans))

# begins program
stair_case()

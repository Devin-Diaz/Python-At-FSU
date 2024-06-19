'''
A positive integer greater than 1 is said to be prime if it has no divisors other than 1 and itself. A
positive integer greater than 1 is composite if it is not prime. Write a program that asks the user to
enter an integer greater than 1, then displays all of the prime numbers that are less than or equal to
the number entered. The program should work as follows:

    a. Once the user has entered a number, the program should populate a list with all of the
    integers from 2 up through the value entered.

    b. The program should then use a loop to step through the list. The loop should pass each
    element to a function that displays the element whether it is a prime number.
'''

# gets user input of ending bound integer, ensures that input is greater than 1.
def get_number() -> int:
    ans = int(input('Enter num: '))
    while ans < 2: 
        print('Must be greater than 1. Try again.')
        ans = int(input('Enter num: '))
    return ans

# bool function that checks if an integer is prime or not
def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0: return False
    return True

# once we have the user input integer, we will use that bound to populate our list
def populate_list_from_input(num: int) -> list[int]:
    return [x for x in range(2, num + 1)]

# determines which numbers from a list are prime and displays them
def find_prime_numbers() -> None: 
    user_num = get_number()
    list_of_nums = populate_list_from_input(user_num)
    print(f'Prime numbers less than or equal to {user_num}:')
    for n in list_of_nums: 
        if is_prime(n): print(n, end='  ')

# begins program
find_prime_numbers()
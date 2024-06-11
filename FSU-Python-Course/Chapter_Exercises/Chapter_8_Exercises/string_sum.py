'''
Write a program that asks the user to enter a number. The program should display the sum of all the 
digits in the number. For example, if the user enters 2514, the method should return 12, which is the 
sum of 2, 5, 1, and 4.
'''

def sum_of_string() -> int:
    ans = input('Enter number: ')
    str_nums = list(ans)
    nums = [int(x) for x in str_nums]
    print(sum(nums))

sum_of_string()

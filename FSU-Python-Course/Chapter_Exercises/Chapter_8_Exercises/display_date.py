'''
Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. 
It should print the date in the format March 12, 2018.
'''

months = {
    "01": "January",
    "02": "Febuary",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

def user_input():
    ans = input('Enter data in mm/dd/yyyy format: ')
    return ans

def get_day(day):
    nums = list(day)
    if "0" in nums:
        return nums[1]
    else:
        return f'{nums[0] + "" + nums[1]}'

def get_month(month):
    return months[month]

def display_date():
    date = user_input()
    parsed_date = date.split('/')
    day = get_day(parsed_date[1])
    month = get_month(parsed_date[0])
    return f'{month} {day}, {parsed_date[2]}'

print(display_date())
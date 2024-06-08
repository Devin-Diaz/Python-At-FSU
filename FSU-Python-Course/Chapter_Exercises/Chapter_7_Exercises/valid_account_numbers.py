

def user_input() -> int:
    ans = input('Enter account #: ')

    while len(ans) != 7:
        print('Try again, must be 7 digits.')
        ans = input('Enter account #: ')
    
    return int(ans)

def parse_data() -> list[int]:
    account_nums = []

    try:
        with open('account_nums.txt', 'r') as file:
            for line in file:
                account_nums.append(int(line.strip()))

    except FileNotFoundError:
        print("Error: file 'account_nums.txt' was not found")
        return []
    
    return account_nums

def check_account() -> None:
    acc_num = user_input()
    all_account_nums = parse_data()

    if acc_num not in all_account_nums:
        print('Account number is invalid.')
    else:
        print('Valid account number!')

check_account()

    
'''
Write a program that asks the user to enter a store's sales for each day of the week. The amounts
should be stored in a list. Use a loop to calculate the total sales for the week and display the result.
'''

def user_input() -> list[float]:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sales = []
    for i in range(len(days)):
        ans = float(input(f'Enter sales for {days[i]}: '))
        sales.append(ans)
    
    return sales

def calculate_total_sales(total_sales: list) -> float:
    total = 0
    for sale in total_sales:
        total += sale
    
    return total

def store_sales() -> None:
    sales_list = user_input()
    total = calculate_total_sales(sales_list)
    print(f'Total sales for the week are: {total:.3f}')


store_sales()
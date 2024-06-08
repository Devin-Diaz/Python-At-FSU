'''
Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:

The number of shares that Joe purchased was 2,000.
When Joe purchased the stock, he paid $40.00 per share.
Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid
for the stock.

Two weeks later, Joe sold the stock. Here are the details of the sale:
The number of shares that Joe sold was 2,000.
He sold the stock for $42.75 per share.

He paid his stockbroker another commission that amounted to 3 percent of the amount he
received for the stock.

Write a program that displays the following information:
The amount of money Joe paid for the stock.
The amount of commission Joe paid his broker when he bought the stock.
The amount for which Joe sold the stock.
The amount of commission Joe paid his broker when he sold the stock.
Display the amount of money that Joe had left when he sold the stock and paid his broker
(both times). If this amount is positive, then Joe made a profit. If the amount is negative,
then Joe lost money
'''


COMMISSION_RATE = 0.03

originalSharesValue = 2000 * 40.00
firstCommission = originalSharesValue * COMMISSION_RATE

newSharesValue = 2000 * 42.75
profit = newSharesValue - originalSharesValue
secondCommission = newSharesValue * COMMISSION_RATE
finalProfit = profit - secondCommission

print(f'''
Joe paid: ${originalSharesValue:.2f} for the stock 
Broker's first commission when stock was bought: ${firstCommission:.2f}
Joe sold the stock for a total of: ${newSharesValue:.2f}
Joe's profit is ${profit:.2f}
Broker's second commission: ${secondCommission:.2f}
After paying the broker, Joe's profit is: ${finalProfit:.2f}
''')





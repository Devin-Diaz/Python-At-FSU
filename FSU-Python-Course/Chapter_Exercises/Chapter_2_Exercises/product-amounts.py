'''
Write a program that will ask the user to enter the amount of a purchase. The program should then
compute the state and county sales tax. Assume the state sales tax is 5 percent and the county sales
tax is 2.5 percent. The program should display the amount of the purchase, the state sales tax, the
county sales tax, the total sales tax, and the total of the sale (which is the sum of the amount of
purchase plus the total sales tax)
'''

COUNTY_TAX = 0.025
STATE_TAX = 0.05

amount = float(input('Enter amount of purchase: $'))
stateTaxAmount = (amount * STATE_TAX)
countyTaxAmount = (amount * COUNTY_TAX)
totalTaxAmount = stateTaxAmount + countyTaxAmount
finalAmount = totalTaxAmount + amount

print(f'''
Original amount: ${amount:.2f}
state tax: ${stateTaxAmount:.2f}
county tax: ${countyTaxAmount:.2f}
total tax: ${totalTaxAmount:.2f}
Total sale is ${finalAmount:.2f}
''')

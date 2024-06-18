'''
RetailItem Class - Write a class named RetailItem that holds data about an item in a retail store. The
class should store the following data in attributes: item description, units in inventory, and price.
Once you have written the class, write a program that creates three RetailItem objects with arbitrary
data and prints them.
'''

class RetailItem:
    def __init__(self, description=None, units=0, price=0) -> None:
        self.description = description
        self.units = units
        self.price = price
    
    
    def to_string(self) -> str:
        return f'Item description: {self.description} | Total units {self.units} | Item Price: {self.price}'


# r1 = RetailItem('Tv Remote', 5, 10.99)
# r2 = RetailItem('Computer', 3, 450.99)
# r3 = RetailItem('Phone Case', 10, 21.99)

# item_list = [r1, r2, r3]

# for item in item_list:
#     print(item.to_string())

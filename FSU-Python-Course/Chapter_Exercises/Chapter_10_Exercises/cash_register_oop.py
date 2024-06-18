'''
Cash Register - This exercise assumes you have created the RetailItem class (above). Create a
CashRegister class that can be used with the RetailItem class. The CashRegister class should be able
to internally keep a list of RetailItem objects.
The class should have the following methods:

A method named purchase_item that accepts a RetailItem object as an argument. Each time
the purchase_item method is called, the RetailItem object that is passed as an argument
should be added to the list.

A method named get_total that returns the total price of all the RetailItem objects stored in
the CashRegister object's internal list.
 A method named show_items that displays data about the RetailItem objects stored in the
CashRegister object's internal list.

A method named clear that should clear the CashRegister object's internal list.
Demonstrate the CashRegister class in a program that allows the user to select several items for
purchase. When the user is ready to check out, the program should display a list of all the items he
or she has selected for purchase, as well as the total price.

'''
from retail_item_oop import RetailItem

class CashRegister:
    def __init__(self) -> None:
        self.items = []
    
    def purchase_item(self, retail_item):
        self.items.append(retail_item)
    
    def get_total(self):
        return sum(item.price for item in self.items)
    
    def show_items(self):
        if len(self.items) == 0: 
            print('Empty register.')
            return

        for item in self.items:
            print(item.to_string()) 
    
    def clear_items(self):
        self.items.clear()

re1 = RetailItem("item1", 10, 15.99)
re2 = RetailItem("item2", 5, 10.99)
re3 = RetailItem("item3", 10, 15.99)

register = CashRegister()

register.purchase_item(re1)
register.purchase_item(re2)
register.show_items()

print(f"Total: ${register.get_total():.2f}")

register.clear_items()

register.show_items()
print(f"Total: ${register.get_total():.2f}")

    

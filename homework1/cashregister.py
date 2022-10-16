class CashRegister():

    def __init__(self, total_items, discount):
        self.total_items = total_items
        self.discount = discount
        self.total_price = 0

    def add_item(self, item, price):
        self.total_items[item] = price

    def remove_item(self, item):
        del self.total_items[item]

    def get_total(self):
        self.total_price = sum(self.total_items.values())
        return self.total_price

    def apply_discount(self):
        if self.discount > 0:
            self.total_price = self.get_total() * self.discount
            print(f'Total price after discount is {self.total_price}')
        else:
            print(f'No discount, total price is {self.get_total()}')

    def show_items(self):
        for item, price in self.total_items.items():
            print(item, price)

    def reset_register(self):
        self.total_price = 0
        self.total_items.clear()
        self.discount = 0

shopping = CashRegister({}, 0.5)
shopping.add_item('bread', 4)
shopping.add_item('cake', 5)
shopping.add_item('pastry', 6)
shopping.show_items()
print("removal of item")
shopping.remove_item('cake')
print("show all items")
shopping.show_items()
print("get new total")
shopping.get_total()
print("get discount")
shopping.apply_discount()
print("show all items")
shopping.show_items()
print("get total")
print(shopping.get_total())

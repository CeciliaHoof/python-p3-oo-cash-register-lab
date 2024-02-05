#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.prices = []
        self.items_quantity = []
    
    def add_item(self, title, price, quantity = 1):
        item_num = quantity
        while item_num > 0:
          self.items.append(title)
          self.prices.append(price)
          item_num -= 1
        self.items_quantity.append(quantity)
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
          discount_amount = (self.total * (self.discount * 0.01))
          self.total = int(self.total - discount_amount)
          print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
      last_price = self.prices[-1]
      item_quantity = self.items_quantity[-1]
      while item_quantity > 0:
        self.total -= last_price
        self.prices.pop(-1)
        self.items.pop(-1)
        item_quantity -= 1

cash_register = CashRegister()
cash_register.add_item("book", 5, 2)
cash_register.void_last_transaction()
print(cash_register.total)

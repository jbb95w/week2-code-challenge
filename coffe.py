# coffee.py
from order import Order

class Coffee:
    all_coffees = []

    def __init__(self, name):
        self.name = name
        Coffee.all_coffees.append(self)
        self.orders_list = []  

    # Name property with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("The Coffee name must be a string.")
        if len(value) < 3:
            raise Exception("The Coffee name must be at least three characters long.")
        self._name = value

    # Return all orders for this coffee
    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    # Return unique customers who ordered this coffee
    def customers(self):
        return list({order.customer for order in self.orders()})

    # Total number of orders for this coffee
    def num_orders(self):
        return len(self.orders())

    # Average price of this coffee
    def average_price(self):
        orders_list = self.orders()
        if not orders_list:
            return 0
        total = sum(order.price for order in orders_list)
        return total / len(orders_list)

    #  for nicer printing
    def __str__(self):
        return f"Coffee({self.name})"
# customer.py
from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name  
        Customer.all_customers.append(self)
        self.orders_list = []  

    # Name property with validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise Exception("Customer name must be between 1 and 15 characters.")
        self._name = value

    # Return all orders for this customer
    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    # Return unique coffees this customer has ordered
    def coffees(self):
        return list({order.coffee for order in self.orders()})

    # Create a new order
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self.orders_list.append(order)
        return order

    # Class method to find the customer who spent the most on a coffee
    @classmethod
    def most_aficionado(cls, coffee):
        orders_for_coffee = [order for order in Order.all_orders if order.coffee == coffee]

        if not orders_for_coffee:
            return None

        spending = {}
        for order in orders_for_coffee:
            spending[order.customer] = spending.get(order.customer, 0) + order.price

        top_customer = max(spending, key=spending.get)
        return top_customer

    # for nicer printing
    def __str__(self):
        return f"Customer({self.name})"

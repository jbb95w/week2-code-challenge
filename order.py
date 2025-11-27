# order.py
class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self.price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

class Coffee:
    all_coffee = []

    def __init__(self, name):
        self.name = name
        Coffee.all_coffee.append(self)
        self.orders_list = []  # orders for this coffee

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


class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name  
        Customer.all_customers.append(self)
        self.orders_list = []

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


if __name__ == "__main__":
    # Customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")

    # Coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    # Orders
    alice.create_order(latte, 4.5)
    alice.create_order(espresso, 3.0)
    bob.create_order(latte, 5.0)
    bob.create_order(latte, 2.5)
    charlie.create_order(espresso, 3.0)

    # Coffee aggregates
    print("Latte num_orders:", latte.num_orders())        
    print("Latte average_price:", latte.average_price()) 
    print("Espresso num_orders:", espresso.num_orders()) 
    print("Espresso average_price:", espresso.average_price()) 

    # Most aficionado
    top_latte = Customer.most_aficionado(latte)
    print("Top Latte customer:", top_latte.name if top_latte else "No one")  

    top_espresso = Customer.most_aficionado(espresso)
    print("Top Espresso customer:", top_espresso.name if top_espresso else "No one")


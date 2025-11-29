# week2-code-challenge
# Coffee Shop

Simple little Python project that shows how customers order coffee and how the program keeps track of everything.

---

## What it does

* You create **Customers**, **Coffees**, and **Orders**.
* Each order links a customer, a coffee, and a price.
* You can check things like how many times a coffee was ordered and who spent the most on it.

---

## How to run it

1. Make sure you have **Python 3.8**.
2. Run the file with the example code:

```bash
python order.py
```

You’ll see things printed like total orders and average price.

---

## Main idea 

* `Customer` makes people.
* `Coffee` makes coffee types.
* `Order` connects a customer and a coffee.

Each new order gets stored in `Order.all_orders`, so the program can calculate things later.

---

## Tiny examples

```python
alice = Customer("Alice")
latte = Coffee("Latte")
alice.create_order(latte, 4.5)
```

Ask the program questions:

```python
latte.num_orders()     
latte.average_price()   
```

---

## Notes

* Coffee names must be at least 3 letters.
* Customer names must be 1–15 characters.
* Keep one class per file (`coffee.py`, `customer.py`, `order.py`) to avoid confusion.

---

Nice little project for learning how objects work in Python.

"""Instantiating A Class"""

"""
This is where we instantiate the class
we defined in classes.py
In other words, we're creating objects
that belong to that class.
"""

from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 12, True)  # Constructor

#  access/set/update attribute values
#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

print(my_pizza.gluten_free)

# Make sals_pizza with size med, 5 toppings, not gf

sals_pizza = Pizza("medium", 5, False)

def price(input_pizza: Pizza) -> float:
    """Compute the price of a pizza."""

    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        cost += 1.00
    return cost

# Calling Function
print(price(my_pizza))
print(price(sals_pizza))

# Classing Method
print(my_pizza.price())
print(sals_pizza.price())

my_pizza.add_toppings(3)
print(my_pizza.toppings)
print(my_pizza.price())

my_second_pizza = my_pizza.add_toppings_new_order(2)
print(my_second_pizza.toppings)

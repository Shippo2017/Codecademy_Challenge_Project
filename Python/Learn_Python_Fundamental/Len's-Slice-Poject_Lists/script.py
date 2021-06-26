# Make Some Pizza
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

# Your boss wants you to do some research on $2 slices. Count the number of occurrences of 2 in the prices list
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Find the length of the toppings list and store it in a variable called num_pizzas
num_pizzas = len(toppings)
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

# Convert our toppings and prices lists into a two-dimensional list called pizza_and_prices
pizza_and_prices = list(zip(prices, toppings))
print(pizza_and_prices)


# Sorting and SLicing Pizzas
# Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
from_cheap_price = sorted(pizza_and_prices)
print(from_cheap_price)

# Store the first element of pizza_and_prices 
cheapest_price = from_cheap_price[0]
print(cheapest_price)

# A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”
priciest_pizza = from_cheap_price[-1]
print(priciest_pizza)

# Remove it from our pizza_and_prices list since the man bought the last slice
print(from_cheap_price.pop(-1))
print(from_cheap_price)

# Add the new peppers pizza topping to our list pizza_and_prices
from_cheap_price.insert(4, (2.5, 'peppers'))
print(from_cheap_price)

# Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = from_cheap_price[:3]
print(three_cheapest)

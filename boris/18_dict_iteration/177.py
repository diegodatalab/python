#
# ! a dict should NOT be assumed to be in order.
# * 177. Iterate over a Dictionary with a for Loop

chinese_food = {
    "Sesame Chicken": 9.99,
     "Boneless Spare Ribs": 7.99,
     "Fried Rice": 1.99
}

for food in chinese_food:
    print(f"the food is {food} and its price is {chinese_food[food]}")
print('-'*50)
print()

pounds_to_kilograms = {
    5: 2.26796,
    10: 4.53592,
    25: 11.3398
}

for _ in pounds_to_kilograms:
    print(f"{_} pounds is equal to {pounds_to_kilograms[_]} kilograms")
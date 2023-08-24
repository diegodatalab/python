#
# * 63. Adding Products To A Dictionary

products = {'phone':100, 'tablet':200, 'laptop':400, 'journal':40}

# print(products)

# product = input("Enter product to check the price: ")

#     # ! dict[key]
# print(products[product])

# print(f"Price of the {product} is {products[product]}")


new_product = input("Enter a product you want to add: ")
new_product_price = input(f"enter the price for {new_product}: ")

products[new_product]=new_product_price

print(f"Product successfully added. Here is an updated list of products {products}")
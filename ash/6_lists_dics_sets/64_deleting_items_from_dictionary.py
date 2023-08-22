products = {'phone':100, 'tablet':200, 'laptop':300, 'journal':5}

print(products)

deleted_product = input('enter the name of product to be deleted: ')

del products[deleted_product]

print(f"product deleted. updated products: {products}")
from producto import Product
from orden import Order

product1 = Product("Shirt", 20.00)
product2 = Product("Skirt", 15.00)
product3 = Product("Pants", 45.00)

products = [product1, product2]

order1 = Order(products)
print(order1)
print(order1.calculate_total())

order2 = Order(products)
order2.add_product(product3)
print(order2)

print(order2.calculate_total())
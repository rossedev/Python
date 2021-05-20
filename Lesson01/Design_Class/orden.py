class Order:
    count_order = 0

    def __init__(self, products):
        Order.count_order += 1
        self.__id_order = Order.count_order
        self.__products = products

    def add_product(self, product):
        self.__products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.__products:
            total += product.get_price()
        return total

    def __str__(self):
        products_str = ""
        for product in self.__products:
            products_str += product.__str__() + " , "

        return "Id order: " + str(self.__id_order) + ", Product: " + products_str

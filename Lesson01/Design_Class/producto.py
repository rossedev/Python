class Product:
    count_products = 0

    def __init__(self, name, price):
        Product.count_products += 1
        self.__id_product = Product.count_products
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def __str__(self):
        return "Id_product: " + str(self.__id_product) + ", Name: " + self.__name + ", Price: " + str(self.__price)
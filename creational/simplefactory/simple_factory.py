from concrete_product_1 import *
from concrete_product_2 import *


class SimpleFactory(object):
    """SimpleFactory to create concret pruduct"""
    def create(self, option):
        if option == "product 1":
            return ConcreteProduct_1()
        elif option == "product 2":
            return ConcreteProduct_2()
        else:
            return None

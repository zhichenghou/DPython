from concret_product_1 import *
from concret_product_2 import *


class SimpleFactory(object):
    """SimpleFactory to create concret pruduct"""
    def create(self, option):
        if option == "product 1":
            return ConcretProduct_1()
        elif option == "product 2":
            return ConcretProduct_2()
        else:
            return None

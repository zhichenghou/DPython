from product import *

class ConcreteProduct_1(Product):
    """a concrete product class to implement common interfaces"""
    def operate(self):
        print "operation implemented by ConcreteProduct_1"
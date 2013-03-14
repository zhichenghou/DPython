#  abstract product

class Product(object):
    """a base class to define common interfaces"""
    def operate(self):
        pass

# concret product

class ConcreteProduct_1(Product):
    """a concret product class to implement common interfaces"""
    def operate(self):
        print "operation implemented by ConcreteProduct_1"

class ConcreteProduct_2(Product):
    """a concret product class to implement common interfaces"""
    def operate(self):
        print "operation implemented by ConcreteProduct_2"
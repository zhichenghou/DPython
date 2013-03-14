#  abstract product

class Product(object):
    """a base class to define common interfaces"""
    def operate(self):
        pass

# concret product

class ConcretProduct_1(Product):
    """a concret product class to implement common interfaces"""
    def operate(self):
        print "operation implemented by ConcretProduct_1"

class ConcretProduct_2(Product):
    """a concret product class to implement common interfaces"""
    def operate(self):
        print "operation implemented by ConcretProduct_2"
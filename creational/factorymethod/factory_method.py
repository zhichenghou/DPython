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

# abstract creator

class Creator(object):
    """a base creator to define factory method"""
    def create(self):
        pass

# concret creator

class ConcreteCreator_1(Creator):
    """ a concret creator to implement factory method"""
    def create(self):
        return ConcretProduct_1()

class ConcreteCreator_2(Creator):
    """ a concret creator to implement factory method"""
    def create(self):
        return ConcretProduct_2()

# use factory method in client

def 
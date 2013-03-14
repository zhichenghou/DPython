from product import *

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
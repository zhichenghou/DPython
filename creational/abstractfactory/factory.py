from product import *

# abstract factory

class AbstractFactory(object):
    def create_product_a(self):
        pass
    def create_product_b(self):
        pass

# concrete factory

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()
    def create_product_b(self):
        return ConcreteProductB2()

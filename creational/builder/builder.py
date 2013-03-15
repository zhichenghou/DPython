from product import *

# abstract builder
class Builder(object):
    def build_part_a(self):
        pass
    def build_part_b(self):
        pass

# concrete builder
class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("1_part_a, ")

    def build_part_b(self):
        self.product.add("1_part_b, ")

    def get_result(self):
        return self.product

class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("2_part_a, ")

    def build_part_b(self):
        self.product.add("2_part_b, ")

    def get_result(self):
        return self.product
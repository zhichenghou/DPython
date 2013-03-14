import random
from product import *
from factory import *

# choice concrete factory manually
fac = ConcreteFactory1()
prod = fac.create_product_a()
prod.operate()


# choice concrete factory randomly
def genfac(n):
    for i in range(n):
        yield random.choice(AbstractFactory.__subclasses__())

facs = [i() for i in genfac(10)]


prods = []
[prods.extend([i.create_product_a(), i.create_product_b()]) for i in facs]

for i in prods:
    i.operate()

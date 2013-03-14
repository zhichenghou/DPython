import random
from product import *
from creator import *

# choice concrete creator manually
mycreator = ConcreteCreator_1()
myproduct = mycreator.create()
myproduct.operate()


# choice concrete creator randomly
def genefac(n):
    for i in range(n):
        yield random.choice(Creator.__subclasses__())

mycreators = [i() for i in genefac(10)]
myproducts = [i.create() for i in mycreators]

for i in myproducts:
    i.operate()

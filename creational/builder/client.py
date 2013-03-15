from builder import *
from director import *

mydirector = Director()
mybuilder1 = ConcreteBuilder1()
mybuilder2 = ConcreteBuilder2()

mydirector.construct(mybuilder1)
mydirector.construct(mybuilder2)

prod1 = mybuilder1.get_result()
prod2 = mybuilder2.get_result()

prod1.show()
prod2.show()

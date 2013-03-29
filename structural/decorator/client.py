from decorator import *

c = ConcreteComponent()
d1 = ConcreteDecoratorA()
d2 = ConcreteDecoratorB()

d1.set_component(c)
d2.set_component(d1)

d2.operation()

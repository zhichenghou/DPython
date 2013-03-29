from abstraction import *
from implementor import *

ab = Abstraction()
imp = ConcreteImplementorA()
ab.set_imp(imp)
ab.operate()

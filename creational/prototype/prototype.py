import copy

# abstract prototype
class Prototype(object):
    def clone(self):
        pass

# concrete prototype
class ConcretePrototype1(Prototype):
    def clone(self):
        return copy.copy(self)

class ConcretePrototype2(Prototype):
    def clone(self):
        return copy.copy(self)
        
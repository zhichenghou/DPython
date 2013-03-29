from component import *

class Decorator(Component):
    def __init__(self):
        self.comp = Component()

    def set_component(self, component):
        self.comp = component

    def operation(self):
        self.comp.operation()

class ConcreteDecoratorA(Decorator):
    def __init__(self):
        super(ConcreteDecoratorA, self).__init__()
        self.added_state = " "

    def operation(self):
        super(ConcreteDecoratorA, self).operation()
        self.added_state += "new state"
        print self.added_state

class ConcreteDecoratorB(Decorator):
    def __init__(self):
        super(ConcreteDecoratorB, self).__init__()
    
    def operation(self):
        super(ConcreteDecoratorB, self).operation()

    def added_behavior(self):
        print "added behavior"      
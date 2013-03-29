class Implementor(object):
    def operation_imp(self):
        pass

class ConcreteImplementorA(Implementor):
    def operation_imp(self):
        print "ConcreteImplementorA operate"

class ConcreteImplementorB(Implementor):
    def operation_imp(self):
        print "ConcreteImplementorB operate"

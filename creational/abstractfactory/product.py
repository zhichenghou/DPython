# abstract product A

class AbstractProductA(object):
    def operate(self):
        pass

# concrete product A

class ConcreteProductA1(AbstractProductA):
    def operate(self):
        print "operate by ConcreteProductA1"

class ConcreteProductA2(AbstractProductA):
    def operate(self):
        print "operate by ConcreteProductA2"

# abstract product B

class AbstractProductB(object):
    def operate(self):
        pass

# concrete product B

class ConcreteProductB1(AbstractProductB):
    def operate(self):
        print "operate by ConcreteProductB1"

class ConcreteProductB2(AbstractProductB):
    def operate(self):
        print "operate by ConcreteProductB2"
class Flyweight(object):
    def operation(self, extrainsicstate):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, extrainsicstate):
        print "concrete flyweight" + str(extrainsicstate)

class UnsharedConcreteFlyweight(Flyweight):
    def operation(self, extrainsicstate):
        print "unshared concrete flyweight" + str(extrainsicstate)

class FlyweightFactory(object):
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, key):
        if self.flyweights.has_key(key):
            return self.flyweights[key]
        else:
            fw = ConcreteFlyweight()
            self.flyweights[key] = fw
            return fw


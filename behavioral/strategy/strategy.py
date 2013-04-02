class Strategy(object):
    def algorithm_interface(self):
        pass

class ConcreteStrategy1(Strategy):
    def algorithm_interface(self):
        print "algorithm 1 "

class ConcreteStrategy2(Strategy):
    def algorithm_interface(self):
        print "algorithm 2 "

class ConcreteStrategy3(Strategy):
    def algorithm_interface(self):
        print "algorithm 3 "

class Context(object):
    def __init__(self, cs):
        self.s = Strategy()
        self.s = cs

    def context_interface(self):
        self.s.algorithm_interface()

def main():
    cs1 = ConcreteStrategy1()
    c = Context(cs1)
    c.context_interface()

    cs2 = ConcreteStrategy2()
    c = Context(cs2)
    c.context_interface()

    cs3 = ConcreteStrategy3()
    c = Context(cs3)
    c.context_interface()

if __name__ == '__main__':
    main()
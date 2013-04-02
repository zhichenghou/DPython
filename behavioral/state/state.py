class State(object):
    def handle(self, context):
        pass

class ConcreteState1(State):
    def handle(self, context):
        next_state = ConcreteState2()
        context.set_state(next_state)

class ConcreteState2(State):
    def handle(self, context):
        next_state = ConcreteState1()
        context.set_state(next_state)

class Context(object):
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state
        print "self.state is " + self.state.__class__.__name__

    def get_state(self):
        return self.state

    def request(self):
        self.state.handle(self)
        
def main():
    s1 = ConcreteState1()
    c = Context(s1)
    c.request()
    c.request()
    c.request()
    c.request()

if __name__ == '__main__':
    main()
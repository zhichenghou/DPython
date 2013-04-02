class Originator(object):
    def __init__(self):
        self.state = " "

    def change_state(self, state):
        self.state = state

    def show(self):
        print self.state

    def set_memento(self, memento):
        self.state = memento.state

    def create_memento(self):
        return Memento(self.state)

class Memento(object):
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state


class Craetaker(object):
    def set_memento(self, memento):
        self.memento = memento
    def get_memento(self):
        return self.memento

def main():
    o = Originator()
    o.change_state("state 1")
    o.show()
    c = Craetaker()
    c.set_memento(o.create_memento())

    o.change_state("state 2")
    o.show()

    o.set_memento(c.get_memento())
    o.show()

if __name__ == '__main__':
    main()
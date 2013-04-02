class Subject(object):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

class Observer(object):
    def update(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        super(ConcreteSubject, self).__init__()
        self.state = ""

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

class ConcreteObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.state = ""

    def set_subject(self, subject):
        self.subject = subject

    def get_subject(self):
        return self.subject

    def update(self):
        self.state = self.subject.get_state()
        print self.state

def main():
    s = ConcreteSubject()
 
    c1 = ConcreteObserver(s)
    c2 = ConcreteObserver(s)
    s.attach(c1)
    s.attach(c2)

    s.set_state("I'm back!")
    s.notify()

    s.set_state("I'm leaving!")
    s.notify()


if __name__ == '__main__':
    main()
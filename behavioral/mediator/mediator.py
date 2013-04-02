class Mediator(object):
    def send(self, colleague, message):
        pass

class Colleague(object):
    def __init__(self, mediator):
        self.mediator = mediator
 
class ConcreteMediator(Mediator):
    def set_colleague(self, colleague1, colleague2):
        self.colleague1 = colleague1
        self.colleague2 = colleague2

    def send(self, colleague, message):
        if self.colleague1 is colleague:
            self.colleague2.notify(message)
        elif self.colleague2 is colleague:
            self.colleague1.notify(message)
        else:
            print "no such colleague"

class ConcreteColleague1(Colleague):
    def send(self, message):
        self.mediator.send(self, message)

    def notify(self, message):
        print "concrete colleague 1 get message: " + message

class ConcreteColleague2(Colleague):
    def send(self, message):
        self.mediator.send(self, message)

    def notify(self, message):
        print "concrete colleague 2 get message: " + message

def main():
    cm = ConcreteMediator()
    cc1 = ConcreteColleague1(cm)
    cc2 = ConcreteColleague2(cm)

    cm.set_colleague(cc1, cc2)

    cc1.send("hello cc2")
    cc2.send("what's up? cc1")

if __name__ == '__main__':
    main()

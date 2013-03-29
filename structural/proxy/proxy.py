class Subject(object):
    def operation(self):
        pass

class RealSubject(Subject):
    def operation(self):
        print "real subject operation"

class Proxy(Subject):
    def __init__(self):
        self.rs = RealSubject()

    def operation(self):
        self.rs.operation()
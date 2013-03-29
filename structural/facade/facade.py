from subsystem import *

class Facade(object):
    def __init__(self):
        self.sub1 = SubSystem1()
        self.sub2 = SubSystem2()
        self.sub3 = SubSystem3()

    def method_a(self):
        self.sub1.method1()
        self.sub3.method3()
        self.sub2.method2()

    def method_b(self):
        self.sub3.method3()
        self.sub2.method2()
        self.sub1.method1()
    
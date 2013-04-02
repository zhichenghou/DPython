class AbstractClass(object):
    def primitive_operation1(self):
        pass

    def primitive_operation1(self):
        pass

    def template_method(self):
        self.primitive_operation1()
        self.primitive_operation2()
        print "!!"

class ConcreteClass1(AbstractClass):
    def primitive_operation1(self):
        print "class 1 operation 1 "
    def primitive_operation2(self):
        print "class 1 operation 2 "

class ConcreteClass2(AbstractClass):
    def primitive_operation1(self):
        print "class 2 operation 1 "
    def primitive_operation2(self):
        print "class 2 operation 2 "

def main():
    c = ConcreteClass1()
    c.template_method()

    c = ConcreteClass2()
    c.template_method()

if __name__ == '__main__':
    main()
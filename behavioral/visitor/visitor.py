class Visitor(object):
    def visit_concrete_element_a(self, concrete_element_a):
        pass
    def visit_concrete_element_b(self, concrete_element_b):
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, concrete_element_a):
        print concrete_element_a.__class__.__name__ + " is visited by " + self.__class__.__name__
    def visit_concrete_element_b(self, concrete_element_b):
        print concrete_element_b.__class__.__name__ + " is visited by " + self.__class__.__name__

class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, concrete_element_a):
        print concrete_element_a.__class__.__name__ + " is visited by " + self.__class__.__name__
    def visit_concrete_element_b(self, concrete_element_b):
        print concrete_element_b.__class__.__name__ + " is visited by " + self.__class__.__name__

class Element(object):
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)
    def operation(self):
        pass

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)
    def operation(self):
        pass

class ObjectStructure(object):
    def __init__(self):
        self.elements = []

    def attach(self, element):
        self.elements.append(element)

    def detach(self, element):
        self.elements.remove(element)

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)

def main():
    o = ObjectStructure()
    o.attach(ConcreteElementA())
    o.attach(ConcreteElementB())

    v1 = ConcreteVisitor1()
    v2 = ConcreteVisitor2()

    o.accept(v1)
    o.accept(v2)

if __name__ == '__main__':
    main()
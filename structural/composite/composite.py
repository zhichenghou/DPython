class Component(object):
    def operation(self,depth):
        pass

    def add(self, component):
        pass

    def remove(self, component):
        pass

# Leaf
class Leaf(Component):
    def operation(self, depth):
        print "-"*depth + "leaf"

# Composite
class Composite(Component):
    def __init__(self):
        self.children = []

    def operation(self, depth):
        print "-"*depth + "composite"
        for c in self.children:
            c.operation(depth+2)

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)


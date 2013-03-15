class Product(object):
    def __init__(self):
        self.parts = "I hava these parts: "

    def add(self, part):
        self.parts += part

    def show(self):
        print self.parts

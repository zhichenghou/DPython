from implementor import *

class Abstraction(object):
    def __init__(self):
        self.imp = Implementor()

    def set_imp(self,conc_imple):
        self.imp = conc_imple;

    def operate(self):
        self.imp.operation_imp()
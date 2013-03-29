from target import *
from adaptee import *


class Adapter(Target):
    def __init__(self):
        self.myadaptee = Adaptee()

    def request(self):
        self.myadaptee.specific_request()

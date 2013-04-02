class Handler(object):
    def set_successor(self, successor):
        self.successor = successor
    def handle_request(self, request):
        pass

class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request >= 0 and request <= 10:
            print "Concrete Handler 1 handled the request " + str(request)
        elif self.successor is not None:
            self.successor.handle_request(request)
        else:
            print "no successor to handle it"

class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request >= 10:
            print "Concrete Handler 2 handled the request " + str(request)
        elif self.successor is not None:
            self.successor.handle_request(request)
        else:
            print "no successor to handle it"

        
        
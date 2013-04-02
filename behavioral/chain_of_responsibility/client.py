from handler import *

h1 = ConcreteHandler1()
h2 = ConcreteHandler2()
h1.set_successor(h2)

for request in range(1,20,2):
    h1.handle_request(request)
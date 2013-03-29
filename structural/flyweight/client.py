from flyweight import *

extrinsicstate = 20
f = FlyweightFactory()
fx = f.get_flyweight("x")
fx.operation(extrinsicstate-1)

fy = f.get_flyweight("y")
fy.operation(extrinsicstate-1)

uf = UnsharedConcreteFlyweight()
uf.operation(extrinsicstate-2)
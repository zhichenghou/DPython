from composite import *

comp1 = Composite()
comp1.add(Leaf())
comp1.add(Leaf())

root = Composite()
leaf = Leaf()
root.add(leaf)
root.add(comp1)

root.operation(2)

root.remove(leaf)
root.operation(2)

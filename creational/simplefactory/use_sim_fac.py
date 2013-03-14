from simple_factory import SimpleFactory

fac = SimpleFactory()
product = fac.create("product 2")
if product is not None:
    product.operate()

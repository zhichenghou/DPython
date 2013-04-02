class Iterator(object):
    def first(self):
        pass
    
    def next(self):
        pass

    def is_done(self):
        pass

    def current_itern(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.current = 0

    def first(self):
        return self.aggregate.get(0)
    def next(self):
        self.current += 1  
        if self.current < self.aggregate.count():
            return self.aggregate.get(self.current)

    def is_done(self):
        if self.current >= self.aggregate.count():
            return True
        else:
            return False

    def current_itern(self):
        return self.aggregate.get(self.current)

class Aggregate(object):
    def create_iterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.list = []

    def get(self, idx):
        return self.list[idx]

    def set(self, idx, value):
        self.list.insert(idx, value)

    def count(self):
        return len(self.list)

    def create_iterator(self):
        return ConcreteIterator(self)


def main():
    a = ConcreteAggregate()
    a.set(0,"no.1")
    a.set(1,"no.2")
    a.set(2,"no.3")

    it = a.create_iterator()

    while not it.is_done():
        print it.current_itern() + " do something"
        it.next()

if __name__ == '__main__':
    main()

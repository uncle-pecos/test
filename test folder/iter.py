class Squares:
    def __init__(self, limit):
        self.limit = limit
        self.n = 1
    def __iter__(self):
        print("iter called")
        return self
    def __next__(self):
        print("next called")
        if self.n < self.limit:
            res = self.n ** 2
            self.n += 1
            return res
        else:      
            raise StopIteration

sq_it = Squares(4)

for i in sq_it:
    print(i)
#for i in iterable:
#    dosmth
#__len__
#__next__() #должна возвращать следующий объект
#__iter__() #должна возвращать итератор

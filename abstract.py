from abc import ABC, abstractmethod

class Absclass(ABC):
    def __init__(self, val):
        self.val = val
        super().__init__()

    @abstractmethod
    def do_smth(self):
        print("abstract implementation")
        self.val += 1
        pass

class B(Absclass):
    def do_smth(self):
        super().do_smth()
        return self.val + 42
    pass

class C(Absclass):
    def do_smth(self):
        super().do_smth()
        return self.val * 10

#a = Absclass(4)
b = B(4)
c = C(4)
print(b.do_smth(), c.do_smth())
from collections import defaultdict

class Duck:
    def __repr__(self):
        return "Duck hehe\n"

class DuckFactory:
    def __call__(self):
        return [Duck()]

d_f = DuckFactory()
ducks = defaultdict(d_f)


for i in (1, 2, 3):
    ducks[i] = ducks[i] * i

print(ducks.items())
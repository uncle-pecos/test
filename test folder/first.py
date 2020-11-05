class Fruit():
    size = 1

    def ch_size(self, newsize):
        self.size = newsize

    def prt(self):
        print ('this is a fruit with size ' + str(self.size))

class Apple(Fruit):
    color = 'red'
    col = 0

    def __init__(self, name):   #инициализирует объект
        print("Apple was made")
        Apple.col += 1
        self.name = name

    def __str__(self):      #возвращает строку (в данном случае строку
        return self.name

   # def __repr__(self):


    def prt(self):
        print ('this is apple with size ' + str(self.size) + ' and color ' + self.color )


apl = Apple('a')
apl.ch_size(2)
print (apl)
apl.prt()
applefarm = [Apple('b'), Apple('c'), Apple('d')]
#for i in applefarm:
#    print(i) 
#print (Apple.col)
setattr(apl, 'size', 4)
print (getattr(apl, 'size'))
delattr(apl, 'name')
print (hasattr(apl, 'name'))

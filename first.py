class Fruit():
    size = 1

    def ch_size(self, newsize):
        self.size = newsize

    def prt(self):
        print ('this is a fruit with size ' + str(self.size))

class Apple(Fruit):
    color = 'red'

    def prt(self):
        print ('this is apple with size ' + str(self.size) + ' and color ' + self.color )


apl = Apple()
apl.ch_size(2)
print (apl.size)
apl.prt()
from abs_figura import Figure

class Circle(Figure):

  def __init__(self, name, a):
    self.name = name
    print ('Создана фигура ' + name + ' с радиусом '+ str(a))

  def sq (self, a):
    sqr = 3.14 * (a**2)
    return sqr
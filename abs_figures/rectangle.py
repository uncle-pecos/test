from abs_figura import Figure

class Rectangle(Figure):
    
  def __init__(self, name, a, b):
    self.name = name
    print ('Создана фигура ' + name + ' со сторонами '+ str(a) + ' и ' + str(b))

  def sq (self, a, b):
    sqr = a*b
    return sqr
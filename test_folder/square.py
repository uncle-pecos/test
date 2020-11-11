from abs_figura import Figure

class Square(Figure):
    
  def __init__(self, name, a):
    self.name = name
    print ('Создана фигура ' + name + ' со стороной '+ str(a))

  def sq (self, a):
    sqr = a**2
    return sqr
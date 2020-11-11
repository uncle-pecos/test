from abs_figura import Figure
import math

class Triangle(Figure):
    
  def __init__(self, name, a):
    self.name = name
    print ('Создана фигура ' + name + ' со стороной '+ str(a))

  def sq (self, a):
    sqr = math.sqrt(3)/4 * a**2
    return sqr
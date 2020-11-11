#from abc import ABC, abstractmethod
from figura import Figure
import math

class Circle(Figure):

  def __init__(self, name, a):
    self.name = name
    print ('Создана фигура ' + name + ' с радиусом '+ str(a))

  def sq (self, a):
    sqr = 3.14 * (a**2)
    return sqr

class Square(Figure):
    
  def __init__(self, name, a):
    self.name = name
    print ('Создана фигура ' + name + ' со стороной '+ str(a))

  def sq (self, a):
    sqr = a**2
    return sqr

class Triangle(Figure):
    
  def __init__(self, name, a):
    self.name = name
    print ('Создана фигура ' + name + ' со стороной '+ str(a))

  def sq (self, a):
    sqr = math.sqrt(3)/4 * a**2
    return sqr


krug = Circle('krug', 2)
print (krug.sq(2))
kvadrat = Square('kvadrat', 2)
print (kvadrat.sq(2))
treugolnik = Triangle('treugolnik', 2)
print (treugolnik.sq(2))
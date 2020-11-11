from abc import ABC, abstractmethod

class Figure(ABC):
  def __init__(self, name, a):
    self.name = name
    print ('Создана фигура', name)

  def sq(self):
    pass

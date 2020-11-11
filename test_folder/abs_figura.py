from abc import ABC, abstractmethod

class Figure(ABC):
  def __init__(self, name, a):
    self.name = name

  def sq(self):
    pass

from models.__init__ import CONN, CURSOR


class Genre:
  all = {}

  def __init__(self, name, id=None):
    self.id = id
    self.name = name
    type(self).all[self.id] = self

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if isinstance(name, str) and len(name):
      self._name = name
    else:
      raise ValueError("Genre name must be a non-empty string.")
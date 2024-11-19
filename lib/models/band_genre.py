from models.band import Band
from models.genre import Genre

class BandGenre:
  all = {}

  def __init__(self, genre, band, id=None):
    self.id = id
    self.genre = genre
    self.band = band
    type(self).all[self.id] = self

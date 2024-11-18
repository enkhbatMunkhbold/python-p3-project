# from models.__init__ import CONN, CURSOR
from models.band import Band
from models.genre import Genre
from models.album import Album

class BandGenre:
  all = {}

  def __init__(self, genre, band):
    self.genre = genre
    self.band = band
    band.genres.append(self)
    genre.bands.append(self)

from models.album import Album
from models.genre import Genre

class AlbumGenre:
  all = {}

  def __init__(self, genre, album, id=None):
    self.id = id
    self.genre = genre
    self.album = album
    type(self).all[self.id] = self
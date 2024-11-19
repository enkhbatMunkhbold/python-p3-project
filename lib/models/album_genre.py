from models.album import Album
from models.genre import Genre

class albumGenre:
  all = {}

  def __init__(self, genre, album):
    self.genre = genre
    self.album = album
    album.genres.append(self)
    genre.albums.append(self)
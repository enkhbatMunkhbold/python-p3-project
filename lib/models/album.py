from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.band import Band

class Album:
  all = {}

  def __init__(self, title, release_year, band_id, genre_id, id=None):
    self.id = id
    self.title = title
    self.release_year = release_year
    self.band_id = band_id
    self.genre_id = genre_id
    type(self).all[self.id] = self

  @property
  def title(self):
    return self._title
  
  @title.setter
  def title(self, title):
    if isinstance(title, str) and len(title) > 1:
      self._title = title
    else:
      raise ValueError("Album title must be a string with lenght more than 1 character.")
  
  @property
  def release_year(self):
    return self._release_year
  
  @release_year.setter
  def release_year(self, release_year):
    if isinstance(release_year, int) and 1900 < release_year <= 2024:
      try:
        self._release_year = int(release_year)
      except ValueError:
        raise ValueError("Album release year must be a four-digit integer.")
      
  @property
  def band_id(self):
    return self._band_id
  
  @band_id.setter
  def band_id(self, band_id):
    if isinstance(band_id, int) and band_id in Band.all():
      try:
        self._band_id = band_id
      except ValueError:
        raise ValueError("Album band ID must be an integer.")
      
  @property
  def genre_id(self):
    return self._genre_id
  
  @genre_id.setter
  def genre_id(self, genre_id):
    if isinstance(genre_id, int) and genre_id in Genre.all():
      try:
        self._genre_id = genre_id
      except ValueError:
        raise ValueError("Album genre ID must be an integer.")
      
  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS albums(
        id INTEGER PRIMARY KEY,
        title TEXT,
        release_year INTEGER,
        band_id INTEGER,
        genre_id INTEGER,
        FOREIGN KEY(band_id) REFERENCES bands(id),
        FOREIGN KEY(genre_id) REFERENCES genres(id))
    """
    CURSOR.execute(sql)
    CONN.commit()
  
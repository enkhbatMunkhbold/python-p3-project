from models.__init__ import CONN, CURSOR
from models.band import Band
from models.genre import Genre

class BandGenre:
  all = []

  def __init__(self, band_id, genre_id):
    self.band_id = band_id
    self.genre_id = genre_id    
    type(self).all[self.id] = self

  @classmethod
  def add(cls, band_id, genre_id):
    band = Band.all.get(band_id)
    genre = Genre.all.get(genre_id)
    if band and genre:
      cls(band_id, genre_id)
    else:
      raise ValueError(f"Band id {band_id} or Genre id {genre_id} not found!")
    
  @classmethod
  def get_all(cls):
    return cls.all

  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS band_genres(
        genre_id INTEGER,
        band_id INTEGER,
        PRIMARY KEY(band_id, genre_id),
        FOREIGN KEY(band_id) REFERENCES band(id),
        FOREIGN KEY(genre_id) REFERENCES genre(id))
    """
    CURSOR.execute(sql)
    CONN.commit()

  @classmethod
  def drop_table(cls):
    sql = """
        DROP TABLE IF EXISTS band_genres;
    """
    CURSOR.execute(sql)
    CONN.commit()
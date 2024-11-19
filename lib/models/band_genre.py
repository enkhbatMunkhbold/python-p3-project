from models.__init__ import CONN, CURSOR

class BandGenre:
  all = {}

  def __init__(self, genre_id, band_id, id=None):
    self.id = id
    self.genre_id = genre_id
    self.band_id = band_id
    type(self).all[self.id] = self

  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS band_genres(
        id INTEGER PRIMARY KEY,
        genre_id INTEGER,
        band_id INTEGER,
        FOREIGN KEY(band_id) REFERENCES band(id),
        FOREIGN KEY(genre_id) REFERENCES genre(id))
    """
  CURSOR.execute(sql)
  CONN.commit()
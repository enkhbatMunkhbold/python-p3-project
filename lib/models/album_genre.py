from models.__init__ import CONN, CURSOR

class AlbumGenre:
  all = {}

  def __init__(self, genre_id, album_id, id=None):
    self.id = id
    self.genre_id = genre_id
    self.album_id = album_id
    type(self).all[self.id] = self

  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS album_genre(
        id INTEGER PRIMARY KEY,
        genre_id INTEGER,
        album_id INTEGER,
        FOREIGN KEY(genre_id) REFERENCES genre(id)
        FOREIGN KEY(album_id) REFERENCES album(id))
    """
    CURSOR.execute(sql)
    CONN.commit()
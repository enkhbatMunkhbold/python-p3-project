from models.__init__ import CONN, CURSOR

class AlbumGenre:
  all = []

  def __init__(self, genre_id, album_id):
    self.genre_id = genre_id
    self.album_id = album_id
    type(self).all[self.id] = self

  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS album_genres(
        genre_id INTEGER,
        album_id INTEGER,
        PRIMARY KEY (genre_id, album_id),
        FOREIGN KEY(genre_id) REFERENCES genre(id),
        FOREIGN KEY(album_id) REFERENCES album(id))
    """
    CURSOR.execute(sql)
    CONN.commit()

  @classmethod
  def drop_table(cls):
    sql = """
        DROP TABLE IF EXISTS album_genres;
    """
    CURSOR.execute(sql)
    CONN.commit()

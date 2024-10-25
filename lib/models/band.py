from models.__init__ import CONN, CURSOR

class Band:
  all = {}

  def __init__(self, name, genre_id, members, id=None):
    self.id = id
    self.name = name
    self.genre_id = genre_id
    self.members = members
    type(self).all[self.id] = self

  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS bands(
        id INTEGER PRIMARY KEY,
        name TEXT,
        genre_id INTEGER,
        members TEXT,
        FOREIGN KEY(genre_id) REFERENCES genres(id))
    """
    CURSOR.execute(sql)
    CONN.commit()

  @classmethod
  def drop_table(cls):
    sql = """
        DROP TABLE IF EXISTS bands;
    """
    CURSOR.execute(sql)
    CONN.commit()
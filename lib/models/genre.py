from models.__init__ import CONN, CURSOR


class Genre:
  all = {}

  def __init__(self, name, id=None):
    self.id = id
    self.name = name
    type(self).all[self.id] = self

  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS genres(
        id INTEGER PRIMARY KEY,
        name TEXT)
    """
    CURSOR.execute(sql)
    CONN.commit()

  @classmethod
  def drop_table(cls):
    sql = """
        DROP TABLE IF EXISTS genres;
    """
    CURSOR.execute(sql)
    CONN.commit()
  
  def save(self):
    sql = """
        INSERT INTO genres(name) VALUES(?)
    """
    CURSOR.execute(sql, (self.name,))
    CONN.commit()
    self.id = CURSOR.lastrowid

  @classmethod
  def create(cls, name):
    genre = cls(name)
    genre.save()
    return genre
  
  def update(self):
    sql = """
        UPDATE genres
        SET name = ?
        WHERE id = ?
    """
    CURSOR.execute(sql, (self.name, self.id))
    CONN.commit()

  def delete(self):
    sql = """
        DELETE FROM genres
        WHERE id = ?
    """
    CURSOR.execute(sql, (self,id,))
    CONN.commit()

  @classmethod
  def get_all_genres(cls):
    sql = """ 
        SELECT id, name
        FROM genres
    """
    CURSOR.execute(sql)
    rows = CURSOR.fetchall()
    genres = {row[0]: Genre(row[1], row[0]) for row in rows}
    return genres

  @classmethod
  def instance_from_db(cls, row):
    genre = cls.all.get(row[0])
    if genre:
      genre.name = row[1]
    else:
      genre = cls(row[1])
      genre.id = row[0]
      cls.all[genre.id] = genre
    return genre

  @classmethod
  def get_all(cls):
    sql = """ 
      SELECT * FROM genres
    """
    rows = CURSOR.execute(sql).fetchall()
    return [cls.instance_from_db(row) for row in rows]

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if isinstance(name, str) and len(name):
      self._name = name
    else:
      raise ValueError("Genre name must be a non-empty string.")
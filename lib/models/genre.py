from models.__init__ import CONN, CURSOR
from models.band import Band
from models.band_genre import BandGenre
from models.album_genre import AlbumGenre

class Genre:
  all = {}

  def __init__(self, id, name):
    self.id = id
    self.name = name
    type(self).all[self.id] = self

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if isinstance(name, str) and len(name) > 2:
      self._name = name
    else:
      raise ValueError("Genre name must be a string with lenght more than 2 characters.")   

  def band_genres(self):
    return [bg for bg in BandGenre.all if bg.genre == self]
  
  def album_genre(self):
    return [ag for ag in AlbumGenre.all if ag.genre == self]

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
    type(self).all[self.id] = self

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
    CURSOR.execute(sql, (self.id,))
    CONN.commit()

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
  
  @classmethod
  def find_by_id(cls, id):
    sql = """
        SELECT * FROM genres
        WHERE id =?
    """
    row = CURSOR.execute(sql, (id,)).fetchone()
    return cls.instance_from_db(row) if row else None

  @classmethod
  def find_by_name(cls, name):
    sql = """ 
      SELECT * FROM genres 
      WHERE name = ?
    """
    row = CURSOR.execute(sql, (name,)).fetchone()
    return cls.instance_from_db(row) if row else None
  
  def bands(self):    
    sql = """
        SELECT * FROM band_genre
        WHERE genre = ?
    """
    CURSOR.execute(sql, (self,),)

    rows = CURSOR.fetchall()
    return [Band.instance_from_db(row) for row in rows]
  
  def albums(self):
    sql = """
        SELECT * FROM album_genre
        WHERE genre = ?
    """
    CURSOR.execute(sql, (self,),)
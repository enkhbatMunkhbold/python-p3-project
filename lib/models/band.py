from models.__init__ import CONN, CURSOR
from lib.models.band_genre import BandGenre

class Band:
  all = {}

  def __init__(self, name, members=[], id=None):
    self.id = id
    self.name = name
    self.members = members
    type(self).all[self.id] = self  

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if isinstance(name, str) and len(name) > 2:
      self._name = name
    else:
      raise ValueError("Band name must be a string with lenght more than 2 characters.")    
   
  def genres_of_band(self):
    return [bg.genre for bg in BandGenre.all if bg.band == self] 


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

  def save(self):
    sql = """
        INSERT INTO bands(name, genre_id, members) VALUES(?, ?, ?)
    """
    CURSOR.execute(sql, (self.name, self.genre_id, self.members))
    CONN.commit()
    self.id = CURSOR.lastrowid
    type(self).all[self.id] = self

  @classmethod
  def create(cls, name, genre_id, members):
    band = cls(name, genre_id, members)
    band.save()
    return band
  
  def update(self):
    sql = """
        UPDATE bands
        SET name = ?, genre_id = ?, members = ?
        WHERE id = ?
    """
    CURSOR.execute(sql, (self.name, self.genre_id, self.members, self.id))
    CONN.commit()

  def delete(self):
    sql = """
        DELETE FROM bands
        WHERE id = ?
    """
    CURSOR.execute(sql, (self.id,))
    CONN.commit()

  @classmethod
  def instance_from_db(cls, row):
    band = cls.all.get(row[0])
    if band:
      band.name = row[1]
      band.genre_id = row[2]
      band.members = row[3]
    else:
      band = cls(row[1], row[2], row[3])
      band.id = row[0]
      cls.all[band.id] = band
    return band
  
  @classmethod
  def get_all(cls):
    sql = """
        SELECT * FROM bands
    """
    rows = CURSOR.execute(sql).fetchall()
    return [cls.instance_from_db(row) for row in rows]
  
  @classmethod
  def find_by_id(cls, id):
    sql = """
        SELECT * FROM bands
        WHERE id = ?
    """
    row = CURSOR.execute(sql, (id,)).fetchone()
    return cls.instance_from_db(row) if row else None
  
  @classmethod
  def find_by_name(cls, name):
    sql = """
        SELECT * FROM bands
        WHERE name = ?
    """
    row = CURSOR.execute(sql, (name,)).fetchone()
    return cls.instance_from_db(row) if row else None
  
  @classmethod
  def get_by_genre(cls, id):
    sql = """
        SELECT * FROM bands
        WHERE genre_id == ?
    """
    
    rows = CURSOR.execute(sql, (id,)).fetchall()
    return [cls.instance_from_db(row) for row in rows]
  
  def albums(self):
    sql = """
        SELECT * FROM albums
        WHERE band_id = ?
    """
    CURSOR.execute(sql, (self.id,),)
 
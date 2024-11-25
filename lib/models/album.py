from models.__init__ import CONN, CURSOR
# from models.genre import Genre
from models.band import Band

class Album:
  all = {}

  def __init__(self, id, title, release_year, band_id):
    self.id = id
    self.title = title
    self.release_year = release_year
    self.band_id = band_id
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
      
  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS albums(
        id INTEGER PRIMARY KEY,
        title TEXT,
        release_year INTEGER,
        band_id INTEGER,
        FOREIGN KEY(band_id) REFERENCES bands(id))
    """
    CURSOR.execute(sql)
    CONN.commit()
  
  @classmethod
  def drop_table(cls):
    sql = """
        DROP TABLE IF EXISTS albums;
    """
    CURSOR.execute(sql)
    CONN.commit()

  def save(self):
    sql = """
        INSERT INTO albums(title, release_year, band_id) VALUES(?, ?, ?)
    """
    CURSOR.execute(sql, (self.title, self.release_year, self.band_id))
    CONN.commit()
    self.id = CURSOR.lastrowid
    type(self).all[self.id] = self

  @classmethod
  def create(cls, id, title, release_year, band_id):
    band = Band.all.get(band_id)
    if band:
      album = cls(id, title, release_year, band_id)
      band.add_album(album)
      return album
    else:
      raise ValueError(f"Band ID {band_id} not found")

  
  def update(self):
    sql = """
        UPDATE alubms
        SET title = ?, release_year = ?, band_id = ?
        WHERE id = ?
    """
    CURSOR.execute(sql, (self.title, self.release_year, self.band_id))
    CONN.commit()

  def delete(self):
    sql = """
        DELETE FROM albums
        WHERE id = ?
    """
    CURSOR.execute(sql, (self.id))
    CONN.commit()

  @classmethod
  def instance_from_db(cls, row):
    album = cls.all.get(row[0])
    if album:
      album.title = row[1]
      album.release_year = row[2]
      album.band_id = row[3]
    else:
      album = cls(row[1], row[2], row[3])
      album.id = row[0]
      cls.all[album.id] = album
    return album
  
  @classmethod
  def get_all(cls):
    sql = """
        SELECT * FROM albums
    """
    rows = CURSOR.execute(sql).fetchall()
    return [cls.instance_from_db(row) for row in rows]
  
  @classmethod
  def find_by_id(cls, id):
    sql = """
        SELECT * FROM albums
        WHERE id = ?
    """
    row = CURSOR.execute(sql, (id,)).fetchone()
    return cls.instance_from_db(row) if row else None
  
  @classmethod
  def find_by_name(cls, name):
    sql = """
        SELECT * FROM albums
        WHERE id = ?
    """
    row = CURSOR.execute(sql, (name,)).fetchone()
    return cls.instance_from_db(row) if row else None
  
  # @classmethod
  # def get_by_genre(cls, id):
  #   sql = """
  #       SELECT * FROM albums
  #       WHERE genre_id == ?
  #   """
  #   rows = CURSOR.execute(sql, (id,)).fetchall()
  #   return [cls.instance_from_db(row) for row in rows]

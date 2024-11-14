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
  
  @classmethod
  def drop_table(cls):
    sql = """
        DROP TABLE IF EXISTS albums;
    """
    CURSOR.execute(sql)
    CONN.commit()

  def save(self):
    sql = """
        INSERT INTO albums(title, release_year, band_id, genre_id) VALUES(?, ?, ?, ?)
    """
    CURSOR.execute(sql, (self.title, self.release_year, self.band_id, self.genre_id))
    CONN.commit()
    self.id = CURSOR.lastrowid
    type(self).all(self.id) = self

  @classmethod
  def create(cls, title, release_year, band_id, genre_id):
    album = cls(title, release_year, band_id, genre_id)
    album.save()
    return album
  
  def update(self):
    sql = """
        UPDATE alubms
        SET title = ?, release_year = ?, band_id = ?, genre_id = ?
        WHERE id = ?
    """
    CURSOR.execute(sql, (self.title, self.release_year, self.band_id, self.genre_id))
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
      album.genre_id = row[4]
    else:
      album = cls(row[1], row[2], row[3], row[4])
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
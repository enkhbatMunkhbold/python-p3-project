from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.band import Band
from models.album import Album
from lib.models.band_genre import BandGenre

def seed_database():
    Genre.drop_table()
    Band.drop_table()
    Album.drop_table()
    BandGenre.drop_table()

    Genre.create_table()
    Band.create_table()
    Album.create_table()
    BandGenre.create_table()

seed_database()
print("Seeded database")
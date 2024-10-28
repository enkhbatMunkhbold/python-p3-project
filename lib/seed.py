from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.band import Band

def seed_database():
    Genre.drop_table()
    Band.drop_table()
    Genre.create_table()
    Band.create_table()

seed_database()
print("Seeded database")
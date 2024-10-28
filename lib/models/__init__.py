import sqlite3

CONN = sqlite3.connect('music_store.db')
CURSOR = CONN.cursor()

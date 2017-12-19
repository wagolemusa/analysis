import sqlite3
from os import path

ROOT = path.dirname(path(__file__))
conn = sqlite3.connect(ROOT + "/sample.db")

c = conn.cursor()
c.execute('SELECT email FROM users')
for row in c.fetchall():
     print row[0]

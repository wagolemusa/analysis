import sqlite3
from os import path
conn = sqlite3.connect("/home/refuge/Desktop/python/pluralsight/simple.db")
c = conn.cursor()
x = 'wise',
c.execute('SELECT email, last, first FROM users WHERE last=?', x)
for row in c.fetchall():
     print row[0], row[1], row[2]

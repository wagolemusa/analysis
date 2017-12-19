import sqlite3
from os import path
conn = sqlite3.connect("/home/refuge/Desktop/python/pluralsight/simple.db")
c = conn.cursor()
employees = [('jill@mail.com', 'Jili', 'AppleTree'),
             ('frank@mail.com', 'Frank','AppleTree'),
             ('desi@mail.com', 'Desi', 'AppleTree'),]
     
c.executemany('Insert into users values(?,?,?)',employees)
conn.commit()
conn.close()
print c.rowcount

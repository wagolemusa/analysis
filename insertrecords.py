import sqlite3
from os import path
conn = sqlite3.connect("/home/refuge/Desktop/python/pluralsight/simple.db")
c = conn.cursor()
x = 'opio@gmail.com', 'fazali', 'bed'
c.execute('Insert into users values(?,?,?)',x)
conn.commit()
conn.close()
print c.rowcount

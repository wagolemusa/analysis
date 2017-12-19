import sqlite3
from os import path
conn = sqlite3.connect("/home/refuge/Desktop/python/pluralsight/simple.db")
c = conn.cursor()
x = 'homie@gmail.com', 
c.execute('Delete from users where email=?',x)
conn.commit()
conn.close()
print c.rowcount

import sqlite3
from os import path
conn = sqlite3.connect("/home/refuge/Desktop/python/pluralsight/simple.db")
c = conn.cursor()
x = 'refuge','homie@gmail.com', 
c.execute('Update users set first=? where email=?',x)
conn.commit()
conn.close()
print c.rowcount

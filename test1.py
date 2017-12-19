import sqlite3
from os import path
conn = sqlite3.connect("/home/refuge/Desktop/python/pluralsight/test.db")
c=conn.cursor()
c.execute('SELECT date, close FROM HistoricalQuotes')
for row in c.fetchall():
     print row[0],row[1]

import sqlite3
import cPickle

class Stock: pass
#create list of object
def getStocks():
     stockList = []
     conn = sqlite3.connect("/home/refuge/Desktop/python/pluralsight/stoks.db")
     c = conn.cursor()
     c.execute('Select date, close, high, low, open, volume, symbol from stockprices')
     for row in c.fetchall():
          stockTuple  = (row[0],row[2],row[3],row[4],row[5],row[6])
          stock = Stock()
          stock.date = row[0]
          stock.close = row[1]
          stock.high = row[2]
          stock.low  = row[3]
          stock.open = row[4]
          stock.volume = row[5]
          stock.symbol = row[6]
          stockList.append(stock)
     return stockList

# initial list
stockList = []
stockList = getStocks()
print len(stockList)

#write pickle
# r = read; w = write; rb = read binary; wb = write binary
my_file = open("stockPick.dat","wb")
#protocol version 0 (ascii),1 (binary), or 2 (binary)

cPickle.dump(stockList,my_file,2)
my_file.close()

#saving data in the file

my_file = open ("objectPickle.dat", "wb")
cPickle.dump(stockList, my_file, 2)
my_file.close()

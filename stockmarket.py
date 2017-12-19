import csv
from datetime import datetime
from dateutil.parser import parse

#Goal: calc value of holding over time
#Goal: calc & sort daily diff of holding over time
#https://finance.google.com/finance?q=nasdaq:goog
#https://www.google.com/finance?q=nyse:f

myDict = {} # key is tuple(symbol, date) value is tuple(open, close)
stockSymbol = "HistoricalQuotes"
fileName = stockSymbol + ".csv"
f = open(fileName, "r")
#reader = csv.reader(f)
next(reader, None) #skip the headers
#Date,open,High,low,Close,volume
for data in reader:
     myDict[(stockSymbol, parse(data[0]))] = (float(data[1]),float(data[4]))

for x in myDict:    
     print x, myDict[x]
print len(myDict)

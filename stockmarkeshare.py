#Adding shares in stack makect
import csv
from datetime import datetime
from dateutil.parser import parse

#Goal: calc value of holding over time
#Goal: calc & sort daily diff of holding over time
#https://finance.google.com/finance?q=nasdaq:goog
#https://www.google.com/finance?q=nyse:f

shares = {"HistoricalQuotes":10,"f":1000}
marketDates = []
myDict = {} # key is tuple(symbol, date) value is tuple(open, close)
for x in shares.keys():
     stockSymbol = x
     fileName = stockSymbol + ".csv"
     f = open(fileName, "r")
     reader = csv.reader(f)
     next(reader, None) #skip the headers
     #Date,open,High,low,Close,volume
     for data in reader:
          if parse(data[0]) not in marketDates:
               marketDates.append(parse(data[0]))
          myDict[(stockSymbol, parse(data[0]))] = (float(data[1]),float(data[4]))

for x in marketDates:
     print x

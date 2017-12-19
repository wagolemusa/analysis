#using total 
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

diff = {}
for date in sorted(marketDates):
     for stk in shares.keys():
          if date in diff:
               diff[date] = diff[date] + (myDict[(stk,date)][1]-myDict[(stk,date)[0]])*shares[stk]
          else:
               diff[date] = (myDict[(stk,date)][1]-myDict[(stk,date)][0])*shares[stk]
for date in sorted(marketDates):
     print date, diff[data]

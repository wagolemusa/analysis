import urllib2

stockList = []
for stk in ['AAPL']:
     url = "http://chartapi.finance.yahoo.com/instrument/1.0/F/chartdata;type=quote;range=1y/csv"
     sourceCode = urllib2.urlopen(url).read()
     splitSource = sourceCode.split('\n')
     for eachLine in splitSource:
     splitLine = eachLine.split(',')
     if len(splitLine) == 6 and len(splitLine[0]) ==8:
          #Date,close, high,low,open,volume
          myTuple = (splitLine[0],splitLine[1],splitLine[5])
          stockList.append(myTuple)

print len(stockList)#it prints the record for one year

for x in stockList: #all elements in stocklist
     print x
     

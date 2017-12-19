import urllib2

stockDict = []
for stk in ['AAPL', 'MSFT']:
     url = "http://chartapi.finance.yahoo.com/instrument/1.0/F/chartdata;type=quote;range=1y/csv"
     sourceCode = urllib2.urlopen(url).read()
     splitSource = sourceCode.split('\n')
     for eachLine in splitSource:
     splitLine = eachLine.split(',')
     if len(splitLine) == 6 and len(splitLine[0]) ==8:
          #Date,close, high,low,open,volume
          myTupleKey = (stk, splitLine[0])
          
          stockDict[myTuplekey] = splitLine[1]

print stockDict[('AAPL', '20170412')] #clossing price
print stockDict[('AAPL', '20170103')]#staring price
print stockDict[('AAPL', '20170412')]
print stockDict[('AAPL', '20170103')]


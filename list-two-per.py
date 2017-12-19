#using list 

import urllib2

count = 0
twoPercent = [] #list
for stk in ['AAPL', 'F', 'MSFT']:
     
     url = "http://chartapi.finance.yahoo.com/instrument/1.0/" + stk +"/chartdata;type=quote;range=1y/csv"
     sourceCode = urllib2.urlopen(url).read()
     splitSource = sourceCode.split('\n')
     for eachLine in splitSource:
          splitLine = eachLine.split(',')
          if len(splitLine) == 6 and len(splitLine[0]) ==8:
               #print splitLine
               cls = float(splitLine[1])
               opn = float(splitLine[4])
               chg = (cls-opn)/opn
               if chg > 0.02:
                    print stk + " " + str(chg) # it corvert the value to string
                    #twoPercent.append(stk + " " + str(chg))
                    twoPercent.append(splitLine[0] + " " + stk + " " + str(chg))#adding date
               count = count + 1

print count
for x in sorted(twoPercent):
     print x

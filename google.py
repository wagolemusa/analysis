import urllib2
import json

stks = ['AAPL', 'F']
for stk in stks:
     url = "http://finance.google.com/finance/info?client=ig&q=" + stk
     gf = urllib2.urlopen(url).read()
     gf = gf.replace("//","")
     json_data = json.loads(gf)[0]
     price = json_data["1_cur"].replace('"','\\|')
     print price

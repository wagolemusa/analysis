with open('aapl.csv', 'r') as f:
     first = f.readline()
     for line in f:
          print line
f.close()

# looking at year stock
max = 0.0
with open('aapl.csv', 'r') as f:
     first = f.readline()
     for line in f:
          splitline = line.split(",")
          if float(splitline[4]) > max:
               max = float(splitline[4])

f.close()
print max

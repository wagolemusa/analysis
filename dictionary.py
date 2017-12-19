import csv

dataFile = "aapl.csv"
f = open(dataFile, "r")
reader = csv.reader(f)
count = 0
for data in reader:
     #print data
     print data[0], data[1]
     count = count + 1
     if count > 10:
          break

import csv
with open('aapl.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

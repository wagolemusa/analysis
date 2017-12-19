import csv
import pygal
from pygal.style import CleanStyle

#downlaod goog.csv, amzn.csv from google finance
stockPrices = {} #key is symbol, value is list of closing price
stockSymbols = ["HistoricalQuotes"]
for symbol in stockSymbols:
     fileName = symbol + ".csv"
     f = open(fileName, "r")
     reader = csv.reader(f)
     reader.next()
     dates = []
     dateset = []
     # Date, open High, Low, Close, Volume
     for x in reader:
          dates.append(x[0])
          dateset.append(float(x[4]))
     stockPrices[symbol]=dateset

line_chart = pygal.Line(style=CleanStyle)
line_chart.title = "Stock Prices"
line_chart.x_labels = dates # list of dates (string)
for x in stockSymbols:
     line_chart.add(symbol, stockPrices[symbol]) #List of closing price (float)
# save the svg to a file
line_chart.render_to_file('stock-chart.svg')

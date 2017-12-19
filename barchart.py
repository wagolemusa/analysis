import pygal
from pygal.style import CleanStyle
from pygal.style import DarkGreenStyle

data1 = {}
data1[1]=10
data1[2]=20
data1[3]=30
data1[4]=25
data1[5]=17

bar_chart = pygal.Bar(style=DarkGreenStyle)
bar_chart.title = "Bar Chart"
bar_chart.x_labels = [1,2,3,4,5] #list
bar_chart.add("data1",data1)
# Save the svg to a file
bar_chart.render_to_file('bar_chart.svg')

from datetime import date

from openpyxl import Workbook
from openpyxl.chart import (
    LineChart,
    Reference,
)
from openpyxl.chart.axis import DateAxis

# create workbook and worksheet
wb = Workbook()
ws = wb.active

# create data
data = []
for i in range(1, 51):
    data.append([i, i**0.5])

# add data to worksheet
rows = [['X', 'Y']]
for row in data:
    rows.append(row)
for row in rows:
    ws.append(row)

# create line chart
c1 = LineChart()
c1.title = "Line Chart"
c1.style = 14
c1.y_axis.title = 'Y'
c1.x_axis.title = 'X'

# add data to chart
data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=51)
c1.add_data(data, titles_from_data=True)

# add chart to worksheet
ws.add_chart(c1, "A10")

# save workbook
wb.save("line.xlsx")
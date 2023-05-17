import openpyxl
from openpyxl.chart import ScatterChart, Reference, Series
from openpyxl.chart.axis import DateAxis

# Load the Excel file
workbook = openpyxl.load_workbook('data.xlsx')
sheet = workbook.active

# Extract data from Excel columns
dates = [cell.value for cell in sheet['A'][1:]]
values = [cell.value for cell in sheet['B'][1:]]

# Convert dates to datetime objects
dates = [date.date() for date in dates]

# Get the action date from the user
action_date = input("Enter the action date (YYYY-MM-DD): ")
action_date = datetime.datetime.strptime(action_date, "%Y-%m-%d").date()

# Create a scatter chart
chart = ScatterChart()
chart.title = "Scatter Chart"
chart.x_axis = DateAxis(crossAx=100)
chart.y_axis.title = "Value"

# Add data series to the chart
series = Series(Reference(sheet, min_col=2, min_row=2, max_row=len(values) + 1),
                xvalues=Reference(sheet, min_col=1, min_row=2, max_row=len(dates) + 1))
series.marker = openpyxl.chart.marker.Marker('circle')

# Set marker colors based on the action date
for i, date in enumerate(dates):
    if date <= action_date:
        series.points[i].graphicalProperties.line.solidFill = openpyxl.styles.colors.Color(rgb='FF0000')  # Red
    else:
        series.points[i].graphicalProperties.line.solidFill = openpyxl.styles.colors.Color(rgb='0000FF')  # Blue

chart.series.append(series)

# Add the chart to the sheet
sheet.add_chart(chart, 'D1')

# Save the Excel file
workbook.save('data.xlsx')

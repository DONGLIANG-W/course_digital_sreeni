import pandas as pd
import matplotlib.pyplot as plt

# Define the CM data as a list of dictionaries
cm_data = [
    {'Date': 'Q1CY22', 'Cost': 3, 'Mode': 'WPP'},
    {'Date': 'Q1CY22', 'Cost': 1, 'Mode': 'IHC'},
    {'Date': 'Q2CY22', 'Cost': 2, 'Mode': 'WPP'}
]

# Create a CM dataframe from the CM data
cm_df = pd.DataFrame(cm_data)

# Convert 'Cost' column to numeric
cm_df['Cost'] = pd.to_numeric(cm_df['Cost'])

# Group the CM dataframe by mode and calculate the total cost
cm_total_cost_by_mode = cm_df.groupby('Mode')['Cost'].sum()
print("CM Total Cost by Mode:")
print(cm_total_cost_by_mode)

# Visualize the cost distribution for each mode using a box plot
cm_df.boxplot(column='Cost', by='Mode')
plt.xlabel('Mode')
plt.ylabel('Cost')
plt.title('CM Cost Distribution by Mode')
plt.show()

# Compare the cumulative cost over time for different modes using line plots
for mode, mode_df in cm_df.groupby('Mode'):
    plt.plot(mode_df['Date'], mode_df['Cost'], label=mode)

plt.xlabel('Date')
plt.ylabel('Cost')
plt.title('CM Cost Over Time')
plt.legend()
plt.show()

# Define the PM data as a list of dictionaries
pm_data = [
    {'Date': 'Q1CY22', 'Cost': 13, 'Mode': 'WPP'},
    {'Date': 'Q1CY22', 'Cost': 11, 'Mode': 'IHC'},
    {'Date': 'Q2CY22', 'Cost': 12, 'Mode': 'WPP'}
]

# Create a PM dataframe from the PM data
pm_df = pd.DataFrame(pm_data)

# Convert 'Cost' column to numeric
pm_df['Cost'] = pd.to_numeric(pm_df['Cost'])

# Group the PM dataframe by mode and calculate the total cost
pm_total_cost_by_mode = pm_df.groupby('Mode')['Cost'].sum()
print("PM Total Cost by Mode:")
print(pm_total_cost_by_mode)

# Visualize the cost distribution for each mode using a box plot
pm_df.boxplot(column='Cost', by='Mode')
plt.xlabel('Mode')
plt.ylabel('Cost')
plt.title('PM Cost Distribution by Mode')
plt.show()

# Compare the cumulative cost over time for different modes using line plots
for mode, mode_df in pm_df.groupby('Mode'):
    plt.plot(mode_df['Date'], mode_df['Cost'], label=mode)

plt.xlabel('Date')
plt.ylabel('Cost')
plt.title('PM Cost Over Time')
plt.legend()
plt.show()

# 1. Calculate the average cost for each mode in the CM and PM datasets:
cm_average_cost_by_mode = cm_df.groupby('Mode')['Cost'].mean()
print("CM Average Cost by Mode:")
print(cm_average_cost_by_mode)

pm_average_cost_by_mode = pm_df.groupby('Mode')['Cost'].mean()
print("PM Average Cost by Mode:")
print(pm_average_cost_by_mode)

# 2. Compare the total cost between CM and PM for each mode:
total_cost_comparison = pd.concat([cm_total_cost_by_mode, pm_total_cost_by_mode], axis=1, keys=['CM Total Cost', 'PM Total Cost'])
print("Total Cost Comparison:")
print(total_cost_comparison)

# 3. Calculate the cumulative cost over time for each mode separately in the CM and PM datasets:
cm_df['Cumulative Cost'] = cm_df.groupby('Mode')['Cost'].cumsum()
pm_df['Cumulative Cost'] = pm_df.groupby('Mode')['Cost'].cumsum()

# Plot cumulative cost over time for CM
plt.plot(cm_df['Date'], cm_df['Cumulative Cost'], label='CM')
plt.xlabel('Date')
plt.ylabel('Cumulative Cost')
plt.title('CM Cumulative Cost Over Time')
plt.legend()
plt.show()

# Plot cumulative cost over time for PM
plt.plot(pm_df['Date'], pm_df['Cumulative Cost'], label='PM')
plt.xlabel('Date')
plt.ylabel('Cumulative Cost')
plt.title('PM Cumulative Cost Over Time')
plt.legend()
plt.show()

# 4. Compare the cost distribution between CM and PM for each mode using overlapping histograms:
# Plot overlapping histograms for CM and PM
plt.hist(cm_df['Cost'], bins=10, alpha=0.5, label='CM')
plt.hist(pm_df['Cost'], bins=10, alpha=0.5, label='PM')
plt.xlabel('Cost')
plt.ylabel('Frequency')
plt.title('Cost Distribution (CM vs PM)')
plt.legend()
plt.show()

# 5.Analyze the monthly cost trends by aggregating the data on a monthly basis:
# Convert 'Date' column to datetime
cm_df['Date'] = pd.to_datetime(cm_df['Date'])
pm_df['Date'] = pd.to_datetime(pm_df['Date'])

# Set 'Date' as the index
cm_df.set_index('Date', inplace=True)
pm_df.set_index('Date', inplace=True)

# Resample to monthly frequency and calculate the sum of costs
cm_monthly_cost = cm_df.resample('M').sum()
pm_monthly_cost = pm_df.resample('M').sum()

# Plot monthly cost trends
plt.plot(cm_monthly_cost.index, cm_monthly_cost['Cost'], label='CM')
plt.plot(pm_monthly_cost.index, pm_monthly_cost['Cost'], label='PM')
plt.xlabel('Month')
plt.ylabel('Cost')
plt.title('Monthly Cost Trends')
plt.legend()
plt.show()

# 6.Perform a correlation analysis to determine the relationship between cost and date:
# Convert 'Date' column to numeric representation (e.g., YYYYMM)
cm_df['Numeric Date'] = cm_df['Date'].str.replace('Q', '').str.replace('CY', '').astype(int)
pm_df['Numeric Date'] = pm_df['Date'].str.replace('Q', '').str.replace('CY', '').astype(int)

# Calculate the correlation coefficient between cost and numeric date
cm_date_cost_corr = cm_df['Cost'].corr(cm_df['Numeric Date'])
pm_date_cost_corr = pm_df['Cost'].corr(pm_df['Numeric Date'])

print("Correlation Coefficient (CM):", cm_date_cost_corr)
print("Correlation Coefficient (PM):", pm_date_cost_corr)


#
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Sample event data
events = {
    'Event A': '2023-01-15',
    'Event B': '2023-02-10',
    'Event C': '2023-03-22',
    'Event D': '2023-05-05'
}

# Step 3: Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Step 4: Convert the dates to datetime objects
event_dates = [mdates.datestr2num(date) for date in events.values()]

# Step 5: Plot the vertical lines or markers
ax.vlines(event_dates, ymin=0, ymax=1, color='blue', linestyle='dashed', label='Events')
# If you prefer markers instead of lines, use the following:
# ax.plot_date(event_dates, [1] * len(event_dates), 'bo', linestyle='dashed', label='Events')

# Step 6: Format the x-axis as dates
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Step 7: Add labels and title
ax.set_xlabel('Date')
ax.set_title('Timeline Events')

# Step 8: Show legend
ax.legend()

# Step 9: Show the plot
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Step 1: Prepare your data
data = {
    'Event': ['Event A', 'Event B', 'Event C', 'Event D'],
    'Date': ['2023-01-15', '2023-02-10', '2023-03-22', '2023-05-05'],
    'Color': ['blue', 'green', 'orange', 'red']  # Different colors for each event
}

df = pd.DataFrame(data)

# Step 2: Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Create the timeline plot with different colored bars for each event
plt.figure(figsize=(10, 5))

for idx, row in df.iterrows():
    plt.barh(row['Event'], width=1, height=0.6, left=row['Date'], color=row['Color'], alpha=0.7)

# Step 4: Format the plot
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xlabel('Date')
plt.ylabel('Event')
plt.title('Timeline of Events')
plt.grid(axis='x')
plt.tight_layout()

# Step 5: Show the plot
plt.show()

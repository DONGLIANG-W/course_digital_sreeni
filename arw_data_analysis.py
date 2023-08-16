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


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Create a pandas DataFrame with event data
data = {
    'Event': ['Event A', 'Event B', 'Event C', 'Event D'],
    'Date': ['2023-01-15', '2023-02-10', '2023-03-22', '2023-05-05']
}

df = pd.DataFrame(data)

# Step 3: Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Step 4: Create a color map for events
color_map = plt.get_cmap('tab10')
num_colors = len(df['Event'].unique())
event_colors = color_map(np.linspace(0, 1, num_colors))

# Step 5: Plot the timeline with different colors for events
plt.figure(figsize=(10, 5))
for i, (event, color) in enumerate(zip(df['Event'].unique(), event_colors)):
    event_df = df[df['Event'] == event]
    plt.scatter(event_df['Date'], np.repeat(i, len(event_df)), color=color, label=event, s=100)

plt.yticks(range(len(df['Event'].unique())), df['Event'].unique())
plt.ylabel('Event')
plt.xlabel('Date')
plt.title('Timeline of Events')
plt.legend(loc='best', bbox_to_anchor=(1.0, 1.0))
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# add label
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
    plt.text(row['Date'], row['Event'], row['Event'], ha='right', va='center', fontsize=12)

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

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QTextEdit

class LogAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log Analyzer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.path_label = QLabel("Enter Log File Path:")
        self.path_edit = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_logs)

        self.blink_label = QLabel()
        self.blink_label.setVisible(False)

        self.load_button = QPushButton("Load and Analyze")
        self.load_button.clicked.connect(self.load_and_analyze)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        self.result_label = QLabel()

        self.layout.addWidget(self.path_label)
        self.layout.addWidget(self.path_edit)
        self.layout.addWidget(self.browse_button)
        self.layout.addWidget(self.blink_label)
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

        self.log_data = None

    def browse_logs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Log Files (*.log *.txt)")
        file_dialog.setOptions(options)
        file_paths, _ = file_dialog.getOpenFileNames(self, "Select Log File(s)")
        
        if file_paths:
            self.log_paths = file_paths
            self.blink_label.setText("\n".join(file_paths))
            self.blink_label.setVisible(True)

    def load_and_analyze(self):
        if not hasattr(self, 'log_paths') or not self.log_paths:
            self.result_label.setText("Please select log file(s) first.")
            return

        try:
            self.log_data = pd.concat((pd.read_csv(path) for path in self.log_paths))
        except Exception as e:
            self.result_label.setText(f"Error loading log data: {e}")
            return

        self.ax.clear()
        self.log_data.plot(x='time', y='value', ax=self.ax)
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Value")

        self.calculate_trend()

        self.canvas.draw()

    def calculate_trend(self):
        # Calculate trend and time to reach a threshold
        # Replace this with your actual calculation

        trend_time = 15  # Placeholder value for demonstration
        if trend_time < 30:
            message = "Preventive maintenance required."
        else:
            message = "PM could be done in next round."

        self.result_label.setText(message)

class FigureCanvas(plt.backends.backend_qt5agg.FigureCanvasQTAgg):
    def __init__(self, figure):
        self.figure = figure
        super().__init__(self.figure)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogAnalyzerApp()
    window.show()
    sys.exit(app.exec_())



import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class LogAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Log Analyzer')
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.lbl_file_path = QLabel('Enter or Browse Log File Path:')
        self.layout.addWidget(self.lbl_file_path)

        self.edit_file_path = QLineEdit()
        self.layout.addWidget(self.edit_file_path)

        self.btn_browse = QPushButton('Browse')
        self.btn_browse.clicked.connect(self.browse_file)
        self.layout.addWidget(self.btn_browse)

        self.btn_plot = QPushButton('Plot and Analyze')
        self.btn_plot.clicked.connect(self.plot_data)
        self.layout.addWidget(self.btn_plot)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.lbl_message = QLabel()
        self.layout.addWidget(self.lbl_message)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def browse_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_paths, _ = file_dialog.getOpenFileNames(self, 'Select Log File(s)', '', 'Log Files (*.log);;All Files (*)')
        self.edit_file_path.setText('\n'.join(file_paths))

    def plot_data(self):
        file_paths = self.edit_file_path.toPlainText().split('\n')
        if not file_paths:
            return

        try:
            data_frames = [pd.read_csv(file_path) for file_path in file_paths]
            # Perform data processing and plotting here
            # Calculate time to reach threshold and decide PM message
            self.lbl_message.setText("Preventive maintenance required." if time_to_reach_threshold < 30 else "PM could be done in next round")

            # Clear previous plot and create a new one
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(data, label='Data')
            ax.plot(trend_line, label='Trend Line')
            ax.set_xlabel('Time')
            ax.set_ylabel('Value')
            ax.legend()

            # Refresh canvas
            self.canvas.draw()
        except Exception as e:
            self.lbl_message.setText(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = LogAnalyzerApp()
    mainWin.show()
    sys.exit(app.exec_())


import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QTextBrowser, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class LogAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Log Analyzer')
        self.setGeometry(100, 100, 800, 600)

        # Widgets
        self.path_label = QLabel('Enter Log File Path:')
        self.path_input = QLineEdit()
        self.browse_button = QPushButton('Browse')
        self.load_button = QPushButton('Load and Analyze')
        self.text_browser = QTextBrowser()

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.message_label = QLabel('Message:')

        # Layouts
        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_label)
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(self.browse_button)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.load_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(path_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.text_browser)
        main_layout.addWidget(self.canvas)
        main_layout.addWidget(self.message_label)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.blink_timer = self.message_label.startTimer(500)  # Blink timer for message label
        self.threshold = 30  # Threshold in days

        # Connect signals
        self.browse_button.clicked.connect(self.browse_files)
        self.load_button.clicked.connect(self.load_and_analyze)
        self.message_label.timerEvent = self.blink_message_label

    def browse_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_paths, _ = file_dialog.getOpenFileNames(self, 'Select Log File(s)', '', 'Log Files (*.log);;All Files (*)', options=options)

        self.text_browser.clear()
        for file_path in file_paths:
            self.text_browser.append(file_path)

    def load_and_analyze(self):
        file_paths = self.text_browser.toPlainText().split('\n')
        dfs = []

        for file_path in file_paths:
            if file_path:
                try:
                    df = pd.read_csv(file_path)  # Modify this for your specific data format
                    dfs.append(df)
                except Exception as e:
                    QMessageBox.critical(self, 'Error', f'Error loading {file_path}: {str(e)}')

        if dfs:
            self.plot_data(dfs)

    def plot_data(self, dataframes):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        for df in dataframes:
            # Process your data here, e.g., plot over time
            # ax.plot(df['time'], df['data'])  # Modify this for your specific data columns

        ax.set_xlabel('Time')
        ax.set_ylabel('Data')
        ax.set_title('Data Over Time')

        self.canvas.draw()

        # Determine if preventive maintenance is required
        if len(dataframes) > 0:  # You may need to adjust this condition based on your data
            time_to_threshold = 15  # Example value, you need to calculate this
            if time_to_threshold < self.threshold:
                message = f'Preventive Maintenance Required: Time to threshold is {time_to_threshold} days.'
            else:
                message = f'PM could be done in next round. Time to threshold is {time_to_threshold} days.'
            self.message_label.setText(message)

    def blink_message_label(self, event):
        if self.message_label.isVisible():
            self.message_label.setVisible(False)
        else:
            self.message_label.setVisible(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogAnalyzerApp()
    window.show()
    sys.exit(app.exec_())


#multilines
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QFileDialog, QLabel

class FileCounterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Counter App")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.file_display = QTextEdit()
        self.layout.addWidget(self.file_display)

        self.scroll_area = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_area)
        self.scroll_area.setLayout(self.scroll_layout)
        self.layout.addWidget(self.scroll_area)

        self.scroll_area.setMaximumHeight(100)
        self.scroll_area.setContentsMargins(0, 0, 0, 0)

        self.scroll_area.setStyleSheet("background-color: lightgray;")

        self.scroll_bar = self.scroll_area.verticalScrollBar()

        self.open_button = QPushButton("Open Files")
        self.open_button.clicked.connect(self.open_files)
        self.layout.addWidget(self.open_button)

        self.count_label = QLabel("Number of Files: 0")
        self.layout.addWidget(self.count_label)

        self.file_count = 0

    def open_files(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        files, _ = file_dialog.getOpenFileNames(self, "Select Files", "", "All Files (*)")

        if files:
            self.file_display.clear()
            self.scroll_layout.clear()
            self.file_count = len(files)
            self.count_label.setText(f"Number of Files: {self.file_count}")

            for file in files:
                self.scroll_layout.addWidget(QLabel(file))
                self.scroll_layout.setAlignment(Qt.AlignTop)

    def update_scroll_bar(self):
        self.scroll_bar.setValue(self.scroll_bar.maximum())

def main():
    app = QApplication(sys.argv)
    window = FileCounterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

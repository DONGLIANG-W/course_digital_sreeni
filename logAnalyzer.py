import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from datetime import timedelta

class LogAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Log Analyzer")

        self.path_label = ttk.Label(root, text="Enter Log File Path:")
        self.path_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.path_input = ttk.Entry(root)
        self.path_input.grid(row=0, column=2, padx=10, pady=10)

        self.browse_button = ttk.Button(root, text="Browse", command=self.browse_files)
        self.browse_button.grid(row=0, column=3, padx=10, pady=10)

        self.path_display = tk.Text(root, height=5, width=40)
        self.path_display.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.load_button = ttk.Button(root, text="Load File", command=self.load_data)
        self.load_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        self.message_label = ttk.Label(root, text="Message:")
        self.message_label.grid(row=4, column=0, padx=10, pady=10)

        self.message_text = tk.StringVar()
        self.message_display = ttk.Label(root, textvariable=self.message_text, font=("Arial", 12, "bold"))
        self.message_display.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

    def browse_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Log Files", "*.log *.txt"), ("All Files", "*.*")])
        self.path_display.delete(1.0, tk.END)
        for file_path in file_paths:
            self.path_display.insert(tk.END, file_path + '\n')

    def load_data(self):
        file_paths = self.path_display.get(1.0, tk.END).strip().split('\n')
        data_frames = []
        for file_path in file_paths:
            if file_path.strip():
                try:
                    df = pd.read_csv(file_path.strip(), sep='\t')  # Modify the reading based on your log file format
                    data_frames.append(df)
                except Exception as e:
                    print("Error loading file:", e)

        if data_frames:
            combined_df = pd.concat(data_frames)
            self.plot_data(combined_df)

    def plot_data(self, data):
        self.figure.clf()
        ax = self.figure.add_subplot(111)
        # Process your data and create the plot here
        # Example:
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")

        # Calculate trend line and time to reach threshold
        trend_line = np.polyfit(x, y, 1)
        threshold_time = (1.0 - trend_line[1]) / trend_line[0]

        if threshold_time < 30:
            self.message_text.set("Preventive maintenance required.")
        else:
            self.message_text.set("PM could be done in next round.")

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = LogAnalyzerApp(root)
    root.mainloop()

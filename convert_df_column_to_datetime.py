import pandas as pd

demo_data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma', 'Charlie'],
    'Age': [25, 30, 35, 27, 32],
    'Country': ['USA', 'Canada', 'UK', 'Australia', 'Germany'],
    'Salary': [50000, 60000, 70000, 55000, 65000],
    'Date': [44562.0, float('nan'), 44563.0, float('nan'), 44563.0]
}

df = pd.DataFrame(demo_data)

df['Date'] = pd.to_datetime(df['Date'], format='%m%d%Y').dt.strftime('%d-%m-%Y')

print(df)

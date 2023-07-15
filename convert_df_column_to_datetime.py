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



# read excel sheets
import pandas as pd

# Specify the path to the Excel file
excel_file_path = 'path/to/your/excel/file.xlsx'

# Read all sheets into a dictionary of dataframes
dfs = pd.read_excel(excel_file_path, sheet_name=None)

# Access each dataframe by sheet name
for sheet_name, df in dfs.items():
    print(f"Sheet: {sheet_name}")
    print(df)
    print()  # Empty line for separation


# adding function for the search
import pandas as pd

# Specify the path to the Excel file
excel_file_path = 'path/to/your/excel/file.xlsx'

# Read all sheets into a dictionary of dataframes
dfs = pd.read_excel(excel_file_path, sheet_name=None)

# Concatenate all dataframes into a single dataframe
combined_df = pd.concat(dfs.values(), ignore_index=True)

# Add columns for each sheet
for sheet_name in dfs.keys():
    combined_df[f'Found in sheet {sheet_name}'] = False

# Set values to True if row is found in each sheet
for sheet_name, df in dfs.items():
    found_col = f'Found in sheet {sheet_name}'
    combined_df[found_col] = combined_df.apply(
        lambda row: row['Name'] in df['Name'].values, axis=1
    )

print(combined_df)

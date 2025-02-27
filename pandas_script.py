import pandas as pd
import numpy as np

# 1. Creating DataFrames
print("### Creating DataFrames ###")
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df, '\n')

# 2. Reading & Writing Data
print("### Reading & Writing Data ###")
# df = pd.read_csv('file.csv')  # Reading CSV
# df.to_csv('output.csv', index=False)  # Writing to CSV

# df = pd.read_excel('file.xlsx')  # Reading Excel
# df.to_excel('output.xlsx', index=False)  # Writing to Excel

# 3. Inspecting Data
print("### Inspecting Data ###")
print(df.head())  # First 5 rows
print(df.tail())  # Last 5 rows
print(df.info())  # Summary of DataFrame
print(df.describe(), '\n')  # Summary statistics

# 4. Selecting Data
print("### Selecting Data ###")
print(df['Name'])  # Selecting a single column
print(df[['Name', 'Age']])  # Selecting multiple columns
print(df.iloc[0])  # Selecting a row by index
print(df.loc[df['Age'] > 25])  # Filtering rows



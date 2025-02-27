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

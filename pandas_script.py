import pandas as pd
import numpy as np

# 1. Creating DataFrames
print("### Creating DataFrames ###")
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df, '\n')
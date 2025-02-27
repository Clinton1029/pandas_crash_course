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


# 5. Adding & Modifying Data
print("### Adding & Modifying Data ###")
df['Bonus'] = df['Salary'] * 0.10  # Adding a new column
print(df, '\n')
df.loc[1, 'Salary'] = 65000  # Modifying a value
print(df, '\n')

# 6. Handling Missing Data
print("### Handling Missing Data ###")
df.loc[2, 'Age'] = np.nan  # Introducing a NaN value
print(df.isnull())  # Check for missing values
print(df.dropna())  # Drop missing values
print(df.fillna(df['Age'].mean()), '\n')  # Fill missing values with mean

# 7. Grouping & Aggregation
print("### Grouping & Aggregation ###")
print(df.groupby('Name')['Salary'].mean(), '\n')

# 8. Sorting & Ordering
print("### Sorting & Ordering ###")
print(df.sort_values(by='Salary', ascending=False), '\n')


# 9. Merging & Joining
print("### Merging & Joining ###")
df2 = pd.DataFrame({'Name': ['Alice', 'Bob', 'David'], 'Department': ['HR', 'IT', 'Finance']})
print(pd.merge(df, df2, on='Name', how='left'), '\n')

# 10. Pivot Tables
print("### Pivot Tables ###")
df_pivot = df.pivot_table(values='Salary', index='Name', aggfunc=np.mean)
print(df_pivot, '\n')

# 11. Applying Functions
print("### Applying Functions ###")
def categorize_age(age):
    return 'Young' if age < 30 else 'Old'
df['Age Group'] = df['Age'].apply(lambda x: categorize_age(x) if pd.notnull(x) else 'Unknown')
print(df, '\n')


# 12. Time Series Handling
print("### Time Series Handling ###")
df['Date'] = pd.date_range(start='1/1/2024', periods=len(df), freq='D')
print(df.set_index('Date'), '\n')

# 13. Visualization
print("### Visualization ###")
import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(df['Salary'], bins=5)
plt.show()


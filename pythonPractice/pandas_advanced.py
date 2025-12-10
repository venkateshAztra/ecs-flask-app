import pandas as pd
# Read csv file 
df = pd.read_csv('sales.csv')
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df['name'])
print(df['amount'])
high_sales = df[df['amount'] > 1000]
print(high_sales)
# ✅ Group by a column, get sum
grouped = df.groupby('name')['amount'].sum()
print(grouped)
print(df.columns)

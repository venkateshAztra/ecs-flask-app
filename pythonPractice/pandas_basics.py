import pandas as pd

df = pd.read_csv('sales.csv')
print(df)

print(df.columns)  # ✅ See columns

customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'customer_name': ['Alice', 'Bob', 'Charlie']
})

# ✅ Match CSV column name
merged = pd.merge(df, customers, left_on='id', right_on='customer_id', how='left')
print(merged)
print(df.columns)

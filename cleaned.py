import pandas as pd
import numpy as np

# 1. Seedha Python ke andar data define kar liya (File na hone ka jhanjhat khatam)
data = {
    'OrderID': [1, 2, 3, 4, 5, 6],
    'CustomerName': ['Rahul', 'Amit', 'Priya', 'Rahul', 'Neha', 'Amit'],
    'Region': ['North', 'South', 'East', 'North', 'West', 'South'],
    'Sales': [500, -200, 350, None, 450, 300],
    'Date': ['2026-10-01', '2026-10-02', '2026-10-03', '2026-10-04', '2026-10-05', '2026-10-06']
}

df = pd.DataFrame(data)

print("--- Original Data ---")
print(df)

# 2. Cleaning Steps
# Missing sales ko average se fill karna
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

# Negative values ko positive karna (.abs())
df['Sales'] = df['Sales'].abs()

# Duplicate rows hatana
df = df.drop_duplicates()

print("\n--- Cleaned Data ---")
print(df)

# 3. Automatic output file generate karna
df.to_csv('cleaned_data.csv', index=False)
print("\nSuccess! 'cleaned_data.csv' file successfully generate ho gayi hai!")
import pandas as pd

# Read the Excel file
df = pd.read_excel('companiesmarketcap.xlsx')

# Convert to Parquet
df.to_parquet('companiesmarketcap.parquet')


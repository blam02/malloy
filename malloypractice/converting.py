import duckdb
#Note the extension below is .tsv for tab separated value, instead of csv
df = duckdb.read_csv('companiesmarketcap.csv', header=True)
#try removing delimiter='\t', header=True
# Print the DataFrame
df.to_parquet('companiesmcap.parquet')
#print(duckdb.sql('DESCRIBE SELECT * FROM df'))


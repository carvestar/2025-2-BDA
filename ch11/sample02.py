import pandas as pd

file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

print('-' * 100)
print(df_raw.head())

print('-' * 100)
print(df_raw.info())
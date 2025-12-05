from io import StringIO
import pandas as pd
import requests
from matplotlib import pyplot as plt

file_name ='./stock_005930_data.csv'
df_raw = pd.read_csv(file_name)
df_raw.set_index('data', inplace = True)

print('-' * 90)
print(df_raw.info())
print('-' * 90)
print(df_raw.head())

df_raw.plot.line()
plt.show()
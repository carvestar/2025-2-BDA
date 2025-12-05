from io import StringIO
import pandas as pd
import requests
from matplotlib import pyplot as plt

file_name ='./stock_005930_data.csv'
df_raw = pd.read_csv(file_name)

df_raw['data_time'] = pd.to_datetime(df_raw['data'])
df_raw = df_raw[df_raw['data_time'].dt.year >= 2025] # 2022
df_raw.drop(columns = ['data_time'], inplace = True)

# 월 단위로 데이터 묶기
df_raw['date_month'] = df_raw['data'].str[:7]
df_raw.set_index('data', inplace = True)

# 중앙값(중간값)
# va1 = 6
# va2 = 10
# 5, 6, 7, 8, 9, 10 , 11 -> 8
# 11 - ((11 - 5) / 2) == 5 + ((11 - 5) / 2)

hi_price = 11
low_price = 5
# hi_price - ((hi_price - low_price) / 2)
df_raw['middle_price'] = df_raw['hi_price'] - ((df_raw['hi_price'] - df_raw['low_price']) / 2)

print('-' * 90)
print(df_raw.info())
print('-' * 90)
print(df_raw.head())

# df_raw.plot.line()
# plt.show()

df_raw.boxplot(column = 'middle_price', by = ['date_month'])
plt.show()
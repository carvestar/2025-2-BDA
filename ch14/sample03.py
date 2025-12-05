import pandas as pd

file_name ='./stock_005930.csv'
df_raw = pd.read_csv(file_name)

print('-' * 50)
print(df_raw.info())
print('-' * 90)
print(df_raw.head())

rename_cols = {
'날짜' : 'data',
'종가' : 'end_price',
'시가' : 'start_price',
'고가' : 'hi_price',
'저가' : 'low_price'
}
drop_cols =['전일비', '거래량']

df_raw.drop(drop_cols, axis = 1, inplace = True)
df_raw.rename(columns = rename_cols, inplace = True)
df_raw.set_index('data', inplace = True)
df_raw.sort_index(inplace = True)

print('-' * 90)
print(df_raw.info())
print('-' * 50)
print(df_raw.head())

df_raw.to_csv('./stock_005930_data.csv')
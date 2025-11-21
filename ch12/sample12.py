import pandas as pd
import matplotlib.pyplot as plt

file_name = './data/seoul-metro-2021.logs.csv'
df_raw = pd.read_csv(file_name)
# timestamp 없애는 방법1
columns = ['station_code', 'people_in', 'people_out']
df_raw = df_raw[columns]

file_name = './data/seoul-metro-station-info.csv'
station_raw = pd.read_csv(file_name)
columns = ['station.code', 'geo.latitude', 'geo.longitude']
station_raw = station_raw[columns]
station_raw = station_raw.set_index('station.code')

print('-' * 100)
print(df_raw)

# timestamp 없애는 방법2
# ds_data = df_raw.groupby('station_code').sum(numeric_only = True)
ds_data = df_raw.groupby('station_code').sum()

print('-' * 100)
print(ds_data)

print('-' * 100)
print(station_raw)

join_data = ds_data.join(station_raw)

print('-' * 100)
print(join_data)

join_data.to_csv('./seoul-inout.csv')
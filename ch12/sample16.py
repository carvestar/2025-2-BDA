import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

'''
퇴근 인원이 가장 많은 장소 확인!!!!!
출근 시간 9시 이전(9시 포함)
퇴근 시간 5시 이후 8시까지
정답
'''

file_name = './data/seoul-metro-2021.logs.csv'
df_raw = pd.read_csv(file_name)

file_name = './data/seoul-metro-station-info.csv'
df_station = pd.read_csv(file_name)
df_station = df_station[['station.code', 'geo.latitude', 'geo.longitude']].set_index('station.code')

print('-' * 100)
print(df_raw.info())                                            # timestamp == object

df_raw['timestamp'] = pd.to_datetime(df_raw['timestamp'])       # datetime64로 변경

print('-' * 100)
print(df_raw.info())                                            # timestamp == datetime64

columns = ['station_code', 'people_in']
data_in = df_raw[df_raw['timestamp'].dt.hour <= 9][columns].groupby('station_code').sum()
data_in = df_raw[df_raw['timestamp'].dt.hour <= 9][['station_code', 'people_out']].groupby('station_code').sum()

# 17 <= hour <= 20
# data_in = df_raw[(17 <= df_raw['timestamp'].df.hour) & (df_raw['timestamp'].df.hour <= 20)][['station_code', 'people_out']].groupby('station_code').sum()==
data_in = df_raw[17 <= df_raw['timestamp'].dt.hour]
data_in = data_in[data_in['timestamp'].dt.hour <= 20]
data_in = data_in[['station_code', 'people_in']].groupby('station_code').sum()

# 위 코드 분할
# data_in = df_raw[df_raw['timestamp'].dt.hour <= 9]
# data_in = data_in[['station_code', 'people_in']]
# data_in = data_in.groupby('station_code').sum()

print('-'*50)
print(data_in.head())

print('-'*50)
print(df_station.head())

join_in = data_in.join(df_station)
# == join_in = df_station.join(data_in)

print('-'*50)
print(join_in.head())

map = folium.Map(location=[37.566621, 126.978208], zoom_start=12)

# 히트맵 플러그인 지도에 추가하기
# HeatMap(data = join_in[['geo.latitude', 'geo.longitude', 'people_in']]).add_to(map) ==
cols = ['geo.latitude', 'geo.longitude', 'people_in']
HeatMap(data = join_in[cols]).add_to(map)
map.show_in_browser()
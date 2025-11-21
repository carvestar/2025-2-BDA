import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

file_name = './seoul-inout.csv'
df_raw = pd.read_csv(file_name)
df_raw = df_raw.set_index('station_code')

print('-' * 100)
print(df_raw)

# 승차 데이터
columns = ['geo.latitude', 'geo.longitude', 'people_in']
data_in = df_raw[columns]

# 하차 데이터
columns = ['geo.latitude', 'geo.longitude', 'people_out']
data_out = df_raw[columns]

print('-' * 100)
print(data_in)

map = folium.Map(location = [37.566621, 126.978208], zoom_start = 12)

# map에 HeatMap 데이터 넣음
HeatMap(data = data_in).add_to(map)
# HeatMap(data = data_out).add_to(map)

# map.show_in_browser()
# map.save('./map-out.html')
map.save('./map-in.html')
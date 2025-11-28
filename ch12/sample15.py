import pandas as pd
import folium
from folium.plugins import HeatMap

'''
퇴근 인원이 가장 많은 장소 확인!!!!!
출근 시간 9시 이전(9시 포함)
퇴근 시간 5시 이후 8시까지
'''

# 데이터 파일 읽기
file_name = './data/seoul-metro-2021.logs.csv'
df_raw = pd.read_csv(file_name)

file_name = './data/seoul-metro-station-info.csv'
df_station = pd.read_csv(file_name)

# 필요한 열만 선택하고, station_code를 인덱스로 설정
df_station = df_station[['station.code', 'geo.latitude', 'geo.longitude']].set_index('station.code')

# timestamp를 datetime 형식으로 변환
df_raw['timestamp'] = pd.to_datetime(df_raw['timestamp'])

# 출근 시간 (9시 이전) 데이터 처리
columns = ['station_code', 'people_in']
data_in = df_raw[df_raw['timestamp'].dt.hour <= 9][columns].groupby('station_code').sum()

# 퇴근 시간 (5시 이후 ~ 8시까지) 데이터 처리
columns_out = ['station_code', 'people_out']
data_out = df_raw[(df_raw['timestamp'].dt.hour >= 17) & (df_raw['timestamp'].dt.hour <= 20)][columns_out].groupby('station_code').sum()

# 출근과 퇴근 데이터 합치기
join_in = data_in.join(df_station)
join_out = data_out.join(df_station)

# 퇴근 인원이 가장 많은 곳을 찾기
most_people_out_station = join_out['people_out'].idxmax()
print(f"퇴근 인원이 가장 많은 역: {most_people_out_station}, 인원: {join_out.loc[most_people_out_station, 'people_out']}")

# 지도 생성 (서울 중심)
map = folium.Map(location=[37.566621, 126.978208], zoom_start=12)

# 출근 시간 히트맵
cols_in = ['geo.latitude', 'geo.longitude', 'people_in']
HeatMap(data=join_in[cols_in]).add_to(map)

# 퇴근 시간 히트맵
cols_out = ['geo.latitude', 'geo.longitude', 'people_out']
HeatMap(data=join_out[cols_out]).add_to(map)

# 지도 출력
map.show_in_browser()
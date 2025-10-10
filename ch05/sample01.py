import os
import pandas as pd

covid_file_path = '../ch04/data/owid-covid-data.csv'
raw_df = pd.read_csv(covid_file_path)

# 원하는 컬럼만
selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']
selected_df = raw_df[selected_columns]

#South Korea
south_korea_df = selected_df[selected_df.location == 'South Korea']
print('-'*50)
print(south_korea_df.head())

#data 컬럼을 index로 지정
index_name = 'date'
korea_date_index_df = south_korea_df.set_index(index_name)
print('-'*50)
print(korea_date_index_df.head())

#저장(dataframe -> csv파일로)
korea_covid_csv_file_name = './data/covid_korea.csv'
if os.path.exists(korea_covid_csv_file_name):
    os.remove(korea_covid_csv_file_name)
korea_date_index_df.to_csv('./data/covid_korea.csv',  sep = '|', encoding = 'utf-8')

#locationd일 미국으로 하고, date를 인덱스로 설정하는 df
#실습!!!!
usa_df = selected_df[selected_df['iso_code'] == 'USA']
print('-'*50)
print(usa_df.head())

# USA 데이터에 index 지정
usa_date_index_df = usa_df.set_index(index_name)
print('-'*50)
print(usa_date_index_df.head())

#저장(usa dataframe -> csv파일로 저장)
usa_covid_csv_file_path = './data/covid_usa.csv'
if os.path.exists(usa_covid_csv_file_path):
    os.remove(usa_covid_csv_file_path)
usa_date_index_df.to_csv(usa_covid_csv_file_path)
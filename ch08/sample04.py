'''
대한민국과 프랑스뿐 아니라 미국과 여러분이 원하는 국가 2개를 추가하여 총 5개국의 올해 확진자 비율을 비교할 수 있는
그래프를 그려 보자. 그리고 어떤 나라가 현재 가장 피해야 할 나라인지 설명해 보자.
'''

import os
import pandas as pd

#코로나 전체 데이터 파일
covid_file_path = '../ch04/data/owid-covid-data.csv'
raw_df = pd.read_csv(covid_file_path)

# 원하는 컬럼만
selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']
selected_df = raw_df[selected_columns]

#date컬럼에 인덱스 설정
selected_date_index_df = selected_df.set_index('date')

#저장(dataframe -> csv파일로)
covid_csv_file_path = '../ch08/data/common_covid.csv'
if os.path.exists(covid_csv_file_path):
    os.remove(covid_csv_file_path)
selected_date_index_df.to_csv(covid_csv_file_path, encoding = 'utf-8')
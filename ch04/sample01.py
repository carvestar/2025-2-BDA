import pandas as pd

covid_file_name = './data/owid-covid-data.csv'
raw_df = pd.read_csv(covid_file_name, sep = ',')

# covid_file_name = './data/sample.csv'
# raw_df = pd.read_csv(covid_file_name, sep = '|')
# covid_file_name = './data/sample_kr.csv'
# raw_df = pd.read_csv(covid_file_name, sep = '|', encoding = 'euc-kr')

# print(raw_df)
# print(type(raw_df))
# print(id(raw_df))
# print(dir(raw_df))

print('-' * 73)
print(raw_df.info())

print('-' * 83)
print(raw_df.head())

# 원하는 컬럼만
selected_columns = ['iso_code', 'location', 'date', 'total_cases', 'population']
selected_df = raw_df[selected_columns]
print('-' * 83)
print(selected_df)

# 데이터에서 국가 확인
# locations = raw_df['location'] ... 밑에 코드와 같은 코드임
locations = selected_df['location']

print('-' * 65)
print(locations)

print('-' * 73)
print(locations.unique())
print(locations.unique().size)

#South Korea
south_korea_df = selected_df[selected_df['location'] == 'South Korea']     # selected_df['location'] == selected_df.location
print('=' * 66)
print(south_korea_df)
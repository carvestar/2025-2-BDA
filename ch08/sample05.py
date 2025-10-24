'''
대한민국과 프랑스뿐 아니라 미국과 여러분이 원하는 국가 2개를 추가하여 총 5개국의 올해 확진자 비율을 비교할 수 있는
그래프를 그려 보자. 그리고 어떤 나라가 현재 가장 피해야 할 나라인지 설명해 보자.
'''

import os
import pandas as pd
from matplotlib import pyplot as plt

def get_covid_data(iso_code, rate_yn):
    file_path = './data/covid_common.csv'
    common_df = pd.read_csv(file_path)

    # 인구비율 기준국가는 미국(USA)에 해당하는 인구수
    common_population_sr = common_df[common_df['iso_code'] == 'USA']['population']
    common_population_value = common_population_sr.iat[0]

    # 현재 iso_code에 해당하는 인구수
    cur_population_sr = common_df[common_df['iso_code'] == iso_code]['population']
    cur_population_value = cur_population_sr.iat[0]

    rate = round(common_population_value / cur_population_value, 2)

    filter_df = common_df[common_df['iso_code'] == iso_code]

    # date 컬럼을 인덱스로 지정
    index_name = 'date'
    index_df = filter_df.set_index(index_name)

    if rate_yn:
        return index_df['total_cases'] * rate
    else:
        return index_df['total_cases']
#end-def

# 절대적인 값에 의해
kor_data = get_covid_data('KOR', False)
usa_data = get_covid_data('USA', False)
fra_data = get_covid_data('FRA', False)
gbr_data = get_covid_data('GBR', False)
pol_data = get_covid_data('POL', False)
index_data = kor_data.index

data = {
    'KOR': kor_data,
    'USA': usa_data,
    'FRA': fra_data,
    'GBR': gbr_data,
    'POL': pol_data
}

df = pd.DataFrame(data, index = index_data)
df[:].plot.line(rot = 45)


# 인구 비율에 맞게
kor_data = get_covid_data('KOR', True)
usa_data = get_covid_data('USA', True)
fra_data = get_covid_data('FRA', True)
gbr_data = get_covid_data('GBR', True)
pol_data = get_covid_data('POL', True)
index_data = kor_data.index

covid_df = pd.DataFrame({
    'KOR': kor_data,
    'USA': usa_data,
    'FRA': fra_data,
    'GBR': gbr_data,
    'POL': pol_data,
}, index = index_data)

covid_df[:].plot.line(rot = 45)
plt.show()
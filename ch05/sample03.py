import pandas as pd
import matplotlib.pyplot as plt
from ch05.common_function import init_matplotlib

# 한글 폰트 깨짐 처리 함수 불러오기
init_matplotlib()

# 전달 받은 파일명에 해당한는 Data리턴 함수
def get_data(filename):
    kor_df = pd.read_csv(filename)
    index_name = 'date'
    kor_index_df = kor_df.set_index(index_name)

    return kor_index_df['total_cases']

kor_data = get_data('./data/covid_kor.csv')
usa_data = get_data('./data/covid_usa.csv')
index_data = kor_data.index

# print('=' * 50)
# print(type(kor_data_df))
# print(type(kor_data_total_cases_series))

# print('=' * 50)
# print(kor_data.head())

# print('=' * 50)
# print(kor_data_total_cases.head())

# print('=' * 50)
# print(usa_data.head())

df = pd.DataFrame(
    {
        # 'KOR' : kor_data,
        # 'USA' : usa_data,
        '대한민국' : kor_data,
        '미국' : usa_data,
    },
    index = index_data
)

df.plot.line()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
from ch05.common_function import init_matplotlib

# 한글 폰트 깨짐 처리 함수 불러오기
init_matplotlib()

# 전달 받은 파일명에 해당한는 Data리턴 함수
def get_data(filename):
    df_raw = pd.read_csv(filename)
    df_raw.set_index('date', inplace=True)

    # TODO: 오류 해결. . .
    population = df_raw['population'].iat[0]   # 아이템 첫 번째 값 가지고 옴

    return {
        'population': population,
        'sr': df_raw['total_cases']
    }

# 2020-01-01 ~ 2020-12-31
kor_data = get_data('../ch05/data/covid_kor.csv')
kor_sr = kor_data['sr']
kor_population = kor_data['population']
kor_index = kor_sr.index

# 2020-03-01 ~ 2021-12-31
hi_data = get_data('./hi_data.csv')
hi_sr = hi_data['sr']
hi_population = hi_data['population']
hi_index = hi_sr.index

# -> 2020-01-01 ~ 2021-12-31의 합집합
data_index = kor_index.union(hi_index)

# 인구 비율 구하기!!!! 과제!!!!
rate = round(kor_population / hi_population, 2)

df = pd.DataFrame(
    {
        '대한민국': kor_sr,
        '하와이': hi_sr * rate,
    },
    index = data_index
)
df.plot.line()
plt.show()

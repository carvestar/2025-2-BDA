import pandas as pd
import matplotlib.pyplot as plt

file_name = '../ch11/data_raw.csv'
df_raw = pd.read_csv(file_name)

# 한글 폰트 깨짐 처리
plt.rc('font', family ='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

target_age = '35-44 years old'
col_age = 'Age'
col_lang = 'LanguageHaveWorkedWith'

# 전체 데이터 중 나이가 '35-44 years old'인 행만 추출
df_filtered = df_raw[df_raw[col_age] == target_age]

# 해당 연령대의 언어 데이터만 추출
ds_data = df_filtered[col_lang].dropna()

ds_data = ds_data.str.split(';')
ds_data = ds_data.explode()

# 데이터 집계
ds_data = ds_data.groupby(ds_data).size()

# 상위 5개 선정
top5_lang = ds_data.nlargest(5)

print('-' * 50)
print(f"[{target_age}] 개발자가 가장 많이 사용하는 언어 Top 5:")
print(top5_lang)
print('-' * 50)

# 시각화
ds_data.nlargest(5).plot.pie(figsize = (8, 8), autopct = '%1.2f%%', startangle = 90,
                             counterclock = False, title = f'{target_age} 개발자가 선호하는 언어 Top 5')

plt.title(f'{target_age} 개발자가 선호하는 언어 Top 5', fontsize=15)
plt.ylabel('')
plt.tight_layout()

# 이미지 저장
plt.savefig('./top5_lang.png')

# 화면 출력
plt.show()
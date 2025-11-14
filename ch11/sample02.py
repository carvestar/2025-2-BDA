import pandas as pd
import matplotlib.pyplot as plt

file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

print('-' * 100)
print(df_raw.info())
print(df_raw.head())

### 개발자 연령대 확인

COLUMN_AGE = 'Age'

sr_data = df_raw['Age']
print('-' * 100)
print(sr_data)

print('-' * 100)
print(sr_data.unique())   # 리스트로 출력

# 중복 삭제
print('-' * 100)
print(sr_data.drop_duplicates())

# df_raw = df_raw.groupby([COLUMN_AGE])   # 그룹바이는 리스트로
print('-' * 100)
print(df_raw)
print(df_raw.size)
print(type(df_raw.size))      # 타입: 시리즈

ds_data = df_raw = df_raw.groupby([COLUMN_AGE]).size()

reindex_column = [
    '65 years or older'
    , '55-64 years old'
    , '45-54 years old'
    , '35-44 years old'
    , '25-34 years old'
    , '18-24 years old'
    , 'Under 18 years old'
    , 'Prefer not to say'
]
ds_data = ds_data.reindex(reindex_column)


# line
ds_data.plot.line(rot = 45)
plt.tight_layout()
plt.show()

# bar
ds_data.plot.bar()
plt.tight_layout()
plt.show()

# barh
ds_data.plot.barh()
plt.tight_layout()
plt.show()
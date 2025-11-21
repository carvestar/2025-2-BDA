import pandas as pd
import matplotlib.pyplot as plt

file_name = '../ch11/data_raw.csv'
df_raw = pd.read_csv(file_name)

COL_LANG = 'LanguageHaveWorkedWith'
ds_data = df_raw[COL_LANG]

print('-' * 100)
print(ds_data)

ds_data = ds_data.str.split(';')

print('-' * 100)
print(ds_data)

ds_data = ds_data.explode()     # .explode(): 리스트 요소를 하나의 요소로 만듦

print('-' * 100)
print(ds_data)

# sample_list = ['a', 'b', 'c']
# sample_list.explode()
# list는 explode() 안 됨 오류

print('-' * 100)
ds_data = ds_data.groupby(ds_data).size()
print(ds_data)

print('-' * 100)
ds_data.nlargest(20).plot.pie(figsize=(10,10), autopct='%1.2f%%')
plt.tight_layout()

plt.savefig('./lang_info.png')

plt.show()